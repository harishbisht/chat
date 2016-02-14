from django.shortcuts import render
from django.http import HttpResponse
from .models import NewPerson, Waiting,Pairing,Message
from django.utils.crypto import get_random_string
import json
from django.utils import timezone
# Create your views here.
def home(request):
	context = {'online':NewPerson.objects.count()}
	return render(request,"chat.html",context)

def get_total_user(request):
	if request.is_ajax():
		try:
			data = json.dumps({'online': NewPerson.objects.count()})
			return HttpResponse(data, content_type='application/json')
		except:
			data = json.dumps({'online':0})
			return HttpResponse(data, content_type='application/json')

def stopsearch(request):
	if request.is_ajax():
		try:
			session_id = request.GET.get('sess')
			NewPerson.objects.filter(session_id=session_id).delete()
		except:
			pass
	data = json.dumps({'flag':0})
	return HttpResponse(data, content_type='application/json')

def connect(request):
	if request.is_ajax():
		session_id = get_random_string(length=32)
		n = NewPerson()
		n.session_id = session_id
		n.save()
		connected = 0
		get_pairing_user = Waiting.objects.all().first()
		if get_pairing_user is not None:
			get_for_foreignkey = NewPerson.objects.get(session_id = get_pairing_user.session_id)
			firstpair = Pairing(user1 = n ,user2 = get_for_foreignkey )
			firstpair.save()
			secondpair = Pairing(user1 = get_for_foreignkey  ,user2 = n)
			secondpair.save()
			n.connected = True
			n.save()
			get_for_foreignkey.connected = True
			get_for_foreignkey.save()
			get_pairing_user.delete()
			connected = 1
		else:
			create_new_waiting = Waiting(session_id = n)
			create_new_waiting.save()
		data = json.dumps({'session_id': session_id,'connected':connected})
		return HttpResponse(data, content_type='application/json')
	else:
		return HttpResponse("Email-id: harishbisht092@gmail.com <br> Github: github.com/harishbisht")


def checkmessages(request):
	if request.is_ajax():
		session_id = request.GET.get('sess')
		try:
			p = NewPerson.objects.get(session_id = session_id)
			p.time =  timezone.now()
			p.save()
		except:
			data = json.dumps({'flag':"nothing here"})
			return HttpResponse(data, content_type='application/json')
			pass
		try:
			p = Pairing.objects.get(user1 = p)
			p = NewPerson.objects.get(session_id = p.user2)
		except:
			if p.connected == True:
				data = json.dumps({'flag':2})
				return HttpResponse(data, content_type='application/json')
			else:
				data = json.dumps({'flag':3})
				return HttpResponse(data, content_type='application/json')

		try:
			m = Message.objects.filter(session_id = p)[0]    #list index out of range error come if no record exist
			message =  m.message
			m.delete()
			data = json.dumps({'message' : message, 'flag':0})
		except:
			data = json.dumps({'flag':1})
		return HttpResponse(data, content_type='application/json')
	else:
		return HttpResponse("Email-id: harishbisht092@gmail.com <br> Github: github.com/harishbisht")
# flag value meaning
# // 0 means your are connected sucessfully  and you get the message 
# // 1 means your are connected but no messages yet
# // 2 means your partner is offline now and not connected
#//3 not connected yet 




def sendmessage(request):
	message =  request.GET.get('msgbox')
	session =  request.GET.get('session')
	person = NewPerson.objects.get(session_id = session)
	msg = Message(session_id= person,message = message)
	msg.save()
	data = json.dumps({'id' : 1})
	return HttpResponse(data, content_type='application/json')


