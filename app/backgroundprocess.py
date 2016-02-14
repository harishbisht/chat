from .models import NewPerson
from django.utils import timezone
import datetime
import threading
def background_process():
	import time
	while 1:
		t = threading.Thread(target=startdelete)
		t.setDaemon(True)
		t.start()
		time.sleep(7)


def deamon_process():
	t = threading.Thread(target=background_process)
	t.setDaemon(True)
	t.start()


def startdelete():
	try:
		obj = NewPerson.objects.all()
		for person in obj:
			if person.time < timezone.now() - datetime.timedelta(seconds = 7):
				person.delete()
	except:
		pass
