from django.http import HttpResponse
import pathlib
from django.shortcuts import render

from visits.models import SiteVisits


this_dir = pathlib.Path(__file__).resolve().parent

def homepage(request, *args, **kwargs):
    queryset = SiteVisits.objects.all()
    path_visits = SiteVisits.objects.filter(path=request.path).count()
    my_title = "bro"
    my_context = {
        "title": my_title,
        "total_visits": queryset.count(),
        "path_visits": path_visits
    }
    SiteVisits.objects.create(path=request.path)

    return render(request, "home.html", my_context)

def old_homepage(request, *args, **kwargs):
    my_title = "blah"
    my_context = {
        "title": my_title
    }

    html_ = """
    <!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
<h1>{title} 1 world</h1> 

</body>
</html>
    """.format(**my_context)
    # html_file_path = this_dir / "home.html"
    # html_ = html_file_path.read_text()


    return HttpResponse(html_)