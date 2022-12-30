from django.shortcuts import render


def praying(request):
    #molitva = "Ги҃ і҆у҃ хе҃ сн҃е бж҃їи помилꙋй мѧ грѣшнаго"
    molitva = "Господи Исусе Христе Сыне Божий, Помилуй Меня Грешного"
    context = {
        "molitva": molitva,
    }  
    return render(request, "run_pray/pray.html", context)