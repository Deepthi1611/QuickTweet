from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.conf import settings


# Create your views here.
def index(request):
    return render(request, 'index.html')

def get_tweets(request):
   tweets = Tweet.objects.all().order_by('-created_at')
   return render(request, 'tweets_list.html', {'tweets':tweets})

@login_required
def create_tweet(request):
    print("LOGIN_URL:", settings.LOGIN_URL)
    form = None
    if(request.method == 'POST'):
        # passing form data and files to form
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            # saves the form but not to the DB as commit is given as False
            tweet = form.save(commit=False)
            tweet.user = request.user
            # saves record to DB
            tweet.save()
            # redirect expects a function from views.py
            return redirect('get_tweets')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def edit_tweet(request, tweet_id):
    form = None
    # user is passed so that logged in user can get his tweets
    # here querying is done based on primary key and user
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if (request.method == 'POST'):
        # passing form data and files to form
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            # saves the form but not to the DB as commit is given as False
            tweet = form.save(commit=False)
            tweet.user = request.user
            # saves record to DB
            tweet.save()
            return redirect('get_tweets')
    else:
        # prefill the form for record for which update operation is being performed
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})  

@login_required
def delete_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if(request.method == 'POST'):
        tweet.delete()
        return redirect('get_tweets')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet}) 

def register(request):
    form = None
    if(request.method == 'POST'):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # set_password is an inbuilt method
            # set_password() method hashes the password before saving it in the database
            # otherwise password is stored as plain text
            user.set_password(form.cleaned_data['password1'])
            user.save()
            # login is default function provided by Django
            # invoke login after the registration
            login(request, user)
            return redirect('get_tweets')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})