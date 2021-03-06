from django.shortcuts import render, redirect
from wordfib.models import WordAndTrue, FakeDefinitions, CorrectGuess
from random import randint, shuffle, choice
from django.core.exceptions import ValidationError

# deploys game with random word and definitions
def home_page(request, from_def=False, name_error=False, def_error=False, choice_error=False, self_error=False):
    rand_word = choice(WordAndTrue.objects.all())
    # word needs at least 2 fake definitions to be displayed
    while rand_word.fakedefinitions_set.count() < 2:
        rand_word = choice(WordAndTrue.objects.all())

    def_list = []
    for defs in (rand_word.fakedefinitions_set.all()):
        def_list.append(defs)

    # include real definition
    def_list.append(rand_word)
    shuffle(def_list)

    # checks to see if user is coming from creation page
    # also handles form validation...kinda hackish I know
    if from_def:
        return render(request, 'home_after_def.html', {'rand_word': rand_word, 'def_list': def_list})
    elif name_error:
        return render(request, 'home.html', {'rand_word': rand_word, 'def_list': def_list, 'error': 'Enter a username!!'})
    elif choice_error:
        return render(request, 'home.html', {'rand_word': rand_word, 'def_list': def_list, 'error': 'Select a definition!'})
    elif def_error:
        return render(request, 'home.html', {'rand_word': rand_word, 'def_list': def_list, 'error': 'Enter a definition!'})
    elif self_error:
        return render(request, 'home.html', {'rand_word': rand_word, 'def_list': def_list, 'error': 'Ah ah ah, bad boy! Don\'t vote on definitions YOU created!'})
    else:
        return render(request, 'home.html', {'rand_word': rand_word, 'def_list': def_list})

# handles voting on the provided word
def vote(request):
    # grab a random word for player to write a fake def.
    rand_word = choice(WordAndTrue.objects.all())
    
    # requires word to have fewer than 3 definitions.
    while rand_word.fakedefinitions_set.count() >= 2:
        rand_word = choice(WordAndTrue.objects.all())

    # enforce lower-case and alpha only
    lower_user = request.POST['username'].lower()
    lower_user = lower_user.lower()
    lower_user = ''.join(c for c in lower_user if c.islower())
    if len(lower_user) == 0:
        return redirect('wordfib:blank_name')
    
    # check if user has already correctly guessed a def.
    user = CorrectGuess.objects.filter(user=lower_user)

    # primary key number of multiple-choice selection
    u_choice = request.POST.get('choice', False)
    if u_choice == False:
        return redirect('wordfib:blank_choice')

    choice_list = []
    choice_list = u_choice.split('-')
    choice_type = choice_list[0]
    choice_uid = choice_list[1]

    # if not already a user, create the user
    if user.count() == 0:
        user = CorrectGuess.objects.create(user=lower_user)
        user.save()
        user.full_clean()
    else:
        user = CorrectGuess.objects.get(user=lower_user)
        
        
    # Handle the scoring and responses of correct vs incorrect guesses
    sent_word = request.POST['word']
    true_def = WordAndTrue.objects.get(word=sent_word)

    #if WordAndTrue.objects.filter(pk=uid).count() == 0:
    #if true_def.id != int(uid):
    if choice_type == "FakeDefinitions":
        fake_def = FakeDefinitions.objects.get(pk=choice_uid)

        # Disallows someone voting on their own definition
        if fake_def.author == lower_user:
            return redirect('wordfib:self_voter')

        fake_def.votes += 2
        fake_def.save()
        current_score = user.score
        get_fake = FakeDefinitions.objects.filter(author=lower_user)
        if get_fake.count() != 0:
            for defs in get_fake:
                current_score += defs.votes 

        return render(request, 'wordfibbd.html', {'author': fake_def, 'current_score': current_score, 'user': user, 'rand_word': rand_word })
    else:
        real_def = WordAndTrue.objects.get(pk=choice_uid)
        user.score += 1
        user.save()
        current_score = user.score
        fake_def = FakeDefinitions.objects.filter(author=lower_user)

        if fake_def.count() != 0:
            for defs in fake_def:
                current_score += defs.votes 
    
        return render(request, 'congrats.html', {'real_def': real_def, 'user': user, 'current_score': current_score, 'rand_word': rand_word}) 

# adds definition to database
def add_def(request, from_add_another=False):
    word = WordAndTrue.objects.get(word=request.POST['word'])

    # tries to reduce/homegenize punctuation and capitilization to reduce
    # some perfect formatting giving away the real definition
    u_def = request.POST['definition'].lower()
    u_def = u_def.rstrip()

    while u_def.startswith(" "):
        u_def = u_def[1:]

    u_def = ''.join(c for c in u_def if c.islower() or c.isdigit() or c == ' ' or c == ',' or c == "'" or c == '.') 

    if len(u_def) == 0:
        return render(request, "create_def.html", {'n_user': request.POST['user'], 'rand_word': request.POST['word']} )

    if u_def[-1] != '.':
        u_def += '.'

    new_def = word.fakedefinitions_set.create(author=request.POST['user'], definition=u_def)

    new_def.save()
    new_def.full_clean()

    if from_add_another:
        return redirect('wordfib:add_yet_another')
    else:
        return redirect('wordfib:from_def')

def scoreboard(request):
    # declare lists for table data
    user_list = []
    cg_score = []
    wf_votes = []
    total_score = []

    # collect user and collect score from correct guesses for each user
    for user in CorrectGuess.objects.all():
        user_list.append(user.user)
        cg_score.append(user.score) 

    # collect score from wordfibbing others for each user
    for author in user_list:
        f_temp = 0
        f_score = FakeDefinitions.objects.filter(author=author) 
        # this collects votes from all definitions created
        for f_def in f_score:
            f_temp += f_def.votes

        wf_votes.append(f_temp)
    

    
    # list comprehension to calculate total votes
    total_score = [(wf + cg) for wf, cg in zip(wf_votes, cg_score)]

    #list comprehension to create lists for each user
    sb_set = [[a, b, c, d] for a, b, c, d in zip(user_list, wf_votes, cg_score, total_score)]

    return render(request, 'scoreboard.html', {'sb_set': sb_set})
     
def add_another(request, pop_again=False):
    
    # grab a random word for player to write a fake def.
    rand_word = choice(WordAndTrue.objects.all())

    while rand_word.fakedefinitions_set.count() >= 2:
        rand_word = choice(WordAndTrue.objects.all())

    thanks_list = ['Thank you very much!', 'Muchas Gracias!', 'Baie Dankie!', 'Merci Beaucoup!', 'Domo Arigato!']
    shuffle(thanks_list)
    thanks = thanks_list[0]

    return render(request, 'populate.html', {'rand_word': rand_word, 'pop_again': pop_again, 'thanks': thanks})
