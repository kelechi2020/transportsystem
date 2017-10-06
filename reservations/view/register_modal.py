from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from reservations.forms import Form_createuser
from reservations.models import Customer, TYPE_CHOICES


class AjaxTemplateMixin():
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'ajax_template_name'):
            split = self.template_name.split('.html')
            split[-1] = '_inner'
            split.append('.html')
            self.ajax_template_name = ''.join(split)
        if request.is_ajax():
            self.template_name = self.ajax_template_name
        return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)

# View for register modal popup


class SmilesView(SuccessMessageMixin, AjaxTemplateMixin, FormView):
    template_name = 'test_form.html'
    form_class = Form_createuser
    success_url = reverse_lazy('home')
    success_message = "Way to go!"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            phone = form.cleaned_data['phone']
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            blood_group = form.cleaned_data['blood_group']

            new = User.objects.create_user(username=email, password=password)
            from pprint import pprint
            pprint(dir(new))
            new.is_active = True
            new.save()
            new = authenticate(username=email, password=password)
            if new is not None:
                login(request, new)
            new_user.save()
        return super(SmilesView, self).post(request, *args, **kwargs)


"""
        if form.has_error(field=errors):
            a = self.field
            pprint(a)

            return self.render_to_response(self.get_context_data(form=form))
"""
"""
    def get_success_message(self, cleaned_data):
        self.success_message

    def form_invalid(self, form):

        If the form is invalid, re-render the context data with the
        #data-filled form and errors.

        return self.render_to_response(self.get_context_data(form=form))

    def errors(self):

        #Returns an ErrorList for this field. Returns an empty ErrorList
        #if there are none.

        return self.form.errors.get(self.name, self.form.error_class())

    def has_error(self, field, code=None):
        if code is None:
            return field in self.errors
        if field in self.errors:
            for error in self.errors.as_data()[field]:
                if error.code == code:
                    return True
        return False

class ContextMixin(object):

    #A default context mixin that passes the keyword arguments received by
    #get_context_data as the template context.


    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
        return kwargs
        """
