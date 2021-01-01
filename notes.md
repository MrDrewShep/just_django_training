### Starting a project, and other commands
* `django-admin startproject <nameofproject> .`
  * Failure to include the `.` will result in unwanted directory structure
* `python manage.py [command(s) here]`
  * `startapp <appname>` creates a new app
  * `runserver` launches a web server
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
  * Rather than build an html form by hand, you can lean on the class `django.forms.ModelForm` and pass that instance as context
  * In the html template you can call `{{ form }}` or `{{ form.as_p }}` which formats each form element with a `<p>` tag for readability

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

### Other notes
* `asgi.py` file is related to asynchronous programming
* Ensure `DEBUG = False` before production