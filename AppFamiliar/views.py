from django.shortcuts import render

from AppFamiliar.models import Familiar


def familia(request):

    familia1 = Familiar(nombre="Sebastian", fecha_nacimiento="2005-10-03", parentezco="Hermano", dni=30545254)
    familia1.save()

    familia2 = Familiar(nombre="Claudio", fecha_nacimiento="2007-04-03", parentezco="Primo", dni=30545123)
    familia2.save()

    familia3 = Familiar(nombre="Sebastian", fecha_nacimiento="1982-05-10", parentezco="Tio", dni=30545456)
    familia3.save()

    contexto = {
        'familia': familia1,
        'familia2': familia2,
        'familia3': familia3,
    }

    return render(request, 'familia.html', contexto)