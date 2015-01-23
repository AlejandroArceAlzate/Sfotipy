from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Track

def track_view(request, tittle):
	track = get_object_or_404(Track, tittle=tittle)
	bio = track.artist.biography

	return render(request, 'track.html', {'track': track, 'bio': bio})
