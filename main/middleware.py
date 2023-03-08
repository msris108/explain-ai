from django.contrib.sessions.models import Session

class SessionHandler:
    """ Middleware that ensures only only session per User """
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if request.user.is_authenticated:
            # Session ID of the newly logged-in User 
            current_session_key = request.user.logged_in_user.session_key

            # Deletes the entry from the Sessions Database if an earlier session existed 
            try:
                if current_session_key and current_session_key != request.session.session_key: 
                    Session.objects.get(session_key=current_session_key).delete()
            except:
                print("flush the sessions")

            # Saves the latest session of the corresponding user    
            request.user.logged_in_user.session_key = request.session.session_key
            request.user.logged_in_user.save()

        response = self.get_response(request)
        return response
    
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DB_NAME"), 
        'USER': env("DB_USER"), 
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': env("DB_HOST"), 
        'PORT': '5432',
    }
}
'''