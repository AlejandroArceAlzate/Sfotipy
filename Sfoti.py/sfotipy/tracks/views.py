import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Track

def track_view(request, tittle):
	track = get_object_or_404(Track, tittle=tittle)
	bio = track.artist.biography

	data = {
		'tittle': track.tittle,
		'order': track.order,
		'album': track.album.tittle,
		'artist': {
			'name': track.artist.first_name,
			'bio': bio,
		}
		
	}

	json_data = json.dumps(data)

	return HttpResponse(json_data, content_type= 'application/json')

	#return render(request, 'track.html', {'track': track, 'bio': bio})
