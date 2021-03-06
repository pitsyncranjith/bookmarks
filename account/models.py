from django.db import models
from django.conf import settings

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	date_of_birth = models.DateField(blank=True, null=True)
	photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

	def __str__(self):
		return 'Profile for user {}'.format(self.user.username)

	"""
		in order to keep your code generic, use the get_user_model() method
		to retrieve the user model and the AUTH_USER_MODEL settings to refer
		to it when defining model's relations to the USER model, instead of
		referring to the auth User model directly.
	"""
