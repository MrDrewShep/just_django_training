### Starting a project, and other commands
* `django-admin startproject <nameofproject> .`
  * Failure to include the `.` will result in unwanted directory structure
* Python gitignore file at: https://github.com/github/gitignore/blob/master/Python.gitignore
* `python manage.py [command(s) here]`
  * `startapp <appname>` creates a new app
  * `runserver` launches a web server
  * `shell` runs a shell with access to the Django project
  * `createsuperuser`

### When changing models, and once upon start of the project
  * `makemigrations <appName>` generates files inside the `migrations/` directory within the app
  * `migrate` applies those migration files

### For a new app within the project
* Register the app by appending to `settings.py` file `INSTALLED_APPS` list

### Urls, within a given app (not the project)
* If needed, create `urls.py` within the app directory
    * The app requires `app_name` to be defined, in it's own `urls.py` file (not the project's `urls.py`)
    * The app's url's can then be included using `include()` in the project's `urls.py`
    * Url resolution goes through the list, so ordering of the url patterns does matter
* Use the `name='giveItAName'` argument to reference that url as such in templates
  * `{% url '<appname>:<giveItAName>' %}`
  * `{% url '<appname>:<giveItAName>' <instance>.<attribute> %}` to pass any additional arguments, e.g. `lead.pk`

### Forms
* If needed, create `forms.py` within the app directory
* Render Method #1, the manual way
  * Create a class with fields that we want to see in the form
  * Pass an instance as context
* Render Method #2, `django.forms.ModelForm`
  * Meta
  * Pass an instance as context
* Notes about the form:
  * In the html template a Django form requires `{% csrf_token %}` be passed for security. #TODO: Find out more about this.
  * In the html template you can call `{{ form }}` or `{{ form.as_p }}` which formats each form element with a `<p>` tag for readability
* `form.is_valid()`
* `form.save()`
* `form.delete()`
* `form.cleaned_data`
* `User = get_user_model()` reads from `settings.AUTH_USER_MODEL`

### Two conventions for templates
| Location for templates | settings.py | views.py |
| --- | --- | --- |
| `templates/` in the project directory | Add `os.path.join(BASE_DIR, "templates")` to `settings.py` file `TEMPLATES` > `DIRS` list | Reference `"todo_list.html"` |
| `<appname>/templates/<appname>/` within each app directory | n/a | Reference `"<appname>/todo_list.html"` |

* For extension of templates:
  * From `templates` folder in the project directory, create `base.html`
  * `{% extends "base.html" %}` and `{% block content %}` and an endblock tag
* Include another file in the base template using `{% include "scripts.html" %}`

### Django Templating Syntax
  * `{{ request.user.is_authenticated }}` returns bool
  * Code looks like `{% for thing in things %}` and `{% endfor %}`
  * Object attributes look like `{{ todo.name }}`

### `django` imports to know
* `models.py`
  * `django.db`
    * `models` module
  * `django.contrib.auth.models` module
    * `AbstractUser` class
* `urls.py`
  * `django.urls`
    * `path`
    * `include`
  * `django.conf`
    * `settings`
  * `django.conf.urls.static`
    * `static`
  * `django.contrib.auth.views` module
    * `LoginView` class
* `views.py`
  * `django.shortcuts`
    * `render` method
    * `redirect` method
    * `reverse` method
  * `django.http`
    * `HttpResponse` class
  * `django.views.generic` module
    * `TemplateViews` class
    * `ListView`, `DetailView`, `UpdateView`, `CreateView`, `DeleteView` classes
  * `django.contrib.auth.forms` module
    * `UserCreationForm` class
* `admin.py`
  * `django.contrib` module
    * `admin` module
* `forms.py`
  * `django`
    * `forms` module
    * `ModelForm` class
  * `django.contrib.auth`
    * `get_user_model` method
* `apps.py`
  * `django.apps`
    * `AppConfig` class
* `tests.py`
  * `django.test`
    * `TestCase` class
* Outbound mail
  * `django.core.mail`
    * `send_mail` method

### Models
* You can reference foreignkey models below your existing model (i.e. which have not yet been declared) by referencing the model in quotations. `mother = models.ForeignKey("Mom")`.
* User model
  * Setup `class User(AbstractUser):` even with just `pass` so that changes can be made in the future. Using `get_user_model()` will not allow for such flexibility in the future.
  * Then tell the project that you've added a custom user model by adding to `settings.py` ... `AUTH_USER_MODEL = '<appname>.User'`
* Model manager == `.objects`

### Views
* View functions must pass `request` as the first parameter
* Class Based Views
  * Inherit from `TemplateView` class
  * Define `template_name` = the template to point to
  * In `urls.py`, in the `path()` import and call the class with `.as_view()`
  * Where applicable, define `queryset` = the regular `<Class>.objects.<query>()`
  * The key of the `context` passed into the template defaults to `object_list` but can be overridden in the class based view by defining `context_object_name`
  * For CreateView
    * No need to pass a `queryset` but instead pass a `form_class`
    * `def get_success_url(self):` for whenever `form.save()` is successful, with either:
      * `return redirect("<template>.html")`
      * `return reverse("<appName>:<url namespace>")`

### Static Files
* In `settings.py`
  * `STATIC_URL = '/static/'`
  * `STATICFILES_DIRS = [ BASE_DIR / 'static']`
  * `STATIC_ROOT = 'static_root'`
* In the project's `urls.py`
  * For production, include the path to the server of static files, e.g. S3
  ```
  if settings.DEBUG:
      urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  ```
* From html templates
  * `{% load static %}`
  * e.g. `<link href="{% static '<filePathWithinStatic>' %} rel="stylesheet">`

### Authentication
* Using Django's built in authentication
  * Add `LoginView` to the project's `urls.py`
  * `LoginView` requires that inside the project's `templates/` directory exist `registration/login.html`
  * Optionally update `settings.py` with `LOGIN_REDIRECT_URL`
  * Optionally use in templates `{% if request.user.is_authenticated %}`
  * Add a class based view into the app for a signup page

### Outbound Mail
* In `settings.py` 
  * In dev `EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'`
  * In prod `EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'`

### Django admin
* Register a model to appear in the admin in each app's `admin.py`
* The model's `__str__` dictates how a record appears

### When releasing to production
* Within `settings.py`:
  * Ensure `DEBUG = False`
  * Update `ALLOWED_HOSTS` with domains

### Recommended VS Code extensions for Django
  * Django, by Robert Solis (batisteo.vscode-django)
  * Django Template, by bibhasdn (bibhasdn.django-html)
  * SQLite, by alexcvzz (alexcvzz.vscode-sqlite)

### Other notes
* `asgi.py` file is related to asynchronous programming
* For styling help checkout:
  * https://tailwindcss.com/docs/installation
  * https://github.com/aniftyco/awesome-tailwindcss
  * https://tailblocks.cc/
  * https://getbootstrap.com/docs/4.3/getting-started/introduction/

### Future reading
  * `.get()` with a dunder passed inside
  * https://docs.djangoproject.com/en/3.1/ref/models/fields/#field-types
  * https://docs.djangoproject.com/en/3.1/howto/static-files/
  * https://docs.djangoproject.com/en/3.1/topics/files/
  * https://docs.djangoproject.com/en/3.1/howto/static-files/deployment/
  * https://docs.djangoproject.com/en/3.1/ref/databases/
  * Decimal v Float https://docs.python.org/3/library/decimal.html#module-decimal
  