from django.shortcuts import render
from django.contrib import messages
import openai
# Create your views here.
def home(request):
    lang_list =['aspnet', 'bash', 'c', 'clike', 'cpp', 'csharp', 'css', 'django', 'html', 'java', 'javascript', 'js-templates', 'markup', 'markup-templating', 'mongodb', 'php', 'powershell', 'python', 'sass', 'scss', 'sql', 'typescript', 'uri', 'visual-basic']
    if request.method == "POST":
        code = request.POST['code']
        lang = request.POST['lang']
        if lang == "Select programming language":
            messages.success(request, "Select appropriate language")
            return render(request, 'home.html', {'lang_list':lang_list, 'code':code, 'lang':lang})
    

        else:
            openai.api_key = "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"
            openai.Model.list()
            try:
                response = openai.Completion.create(
                    engine = 'text-davinci-003',
                    prompt = f"Respond only with code. fix this {lang} code: {code}",
                    temperature = 0,
                    max_tokens = 1000,
                    top_p = 1.0,
                    frequency_penalty = 0.0,
                    presence_penalty = 0.0,
                )
                response =(response["choices"][0]['text']).strip()
                return render(request, 'home.html', {'lang_list':lang_list, 'response':response, 'lang':lang })
            except Exception as e:
                return render(request, 'home.html', {'lang_list':lang_list, 'response':e, 'lang':lang })
        
    return render(request, 'home.html', {'lang_list':lang_list})


def suggest(request):
    return render(request, 'suggest.html', {})