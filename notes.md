### Starting a project, and other commands
* `django-admin startproject <nameofproject> .`
  * Failure to include the `.` will result in unwanted directory structure
* Python gitignore file at: https://github.com/github/gitignore/blob/master/Python.gitignore
* `python manage.py [command(s) here]`
  * `startapp <appname>` creates a new app
  * `runserver` launches a web server

### When changing models, and once upon start of the project
  * `makemigrations` generates files inside the `migrations/` directory within each app
  * `migrate` applies those migration files

### For a new app within the project
* Register the app by appending to `settings.py` file `INSTALLED_APPS` list
* If needed, create `urls.py` within the app directory
    * The app requires `app_name` to be defined, in it's `urls.py` file
    * The app's url's can then be included using `include()` in the project's `urls.py`
    * Url resolution goes through the list, so ordering of the url patterns does matter
* If needed, create `forms.py` within the app directory
  * In the html template a Django form requires `{% csrf_token %}` be passed for security. #TODO: Find out more about this.
  * In the html template you can call `{{ form }}` or `{{ form.as_p }}` which formats each form element with a `<p>` tag for readability
  * Rather than build an html form by hand, you can lean on the class `django.forms.ModelForm` and pass that instance as context
    * `form.is_valid()`
    * `form.save()`
    * `form.delete()`

### Two conventions for templates
| Location for templates | settings.py | views.py |
| --- | --- | --- |
| `templates/` in the project directory | Add `os.path.join(BASE_DIR, "templates")` to `settings.py` file `TEMPLATES` > `DIRS` list | Reference `"todo_list.html"` |
| `<appname>/templates/<appname>/` within each app directory | n/a | Reference `"<appname>/todo_list.html"` |

### Django Templating Syntax
  * `{{ request.user.is_authenticated }}` returns bool
  * Code looks like `{% for thing in things %}` and `{% endfor %}`
  * Object attributes look like `{{ todo.name }}`

### `django` imports
* `django`
  * `forms` module
* `django.urls`
  * `path`
* `django.shortcuts`
  * `render` method
  * `redirect` method
* `django.http`
  * `HttpResponse` class
* `django.apps`
  * `AppConfig` class
* `django.db`
  * `models` module
* `django.test`
  * `TestCase` class

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
* For styling help checkout https://getbootstrap.com/docs/4.3/getting-started/introduction/

### Future reading
  * https://docs.djangoproject.com/en/3.1/howto/static-files/
  * https://docs.djangoproject.com/en/3.1/topics/files/
  * https://docs.djangoproject.com/en/3.1/howto/static-files/deployment/
  * https://docs.djangoproject.com/en/3.1/ref/databases/
  * Decimal v Float https://docs.python.org/3/library/decimal.html#module-decimal
  