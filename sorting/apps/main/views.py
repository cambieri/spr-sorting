from django.template import loader
import sys
from django import http
from django.template.context import Context
from django.shortcuts import render
import json

def nondefault_500_error(request, template_name='500nondefault.html'):
    """
    500 error handler for debug.

    Templates: `500.html`
    Context: sys.exc_info() results
     """
    t = loader.get_template(template_name) # You need to create a 500.html template.
    ltype,lvalue,ltraceback = sys.exc_info()
    sys.exc_clear() #for fun, and to point out I only -think- this hasn't happened at 
                    #this point in the process already
    return http.HttpResponseServerError(t.render(Context({'type':ltype,'value':lvalue,'traceback':ltraceback})))

def index(request):
    icons = []
    icon1 = "M278.939,132.632l-0.641-0.853l0.183-1.97l-0.975,0.091l-0.92-0.092l-0.506,0.415l-0.526,0.234l-0.541,0.053l-0.939-0.271l-1.049,0.468l-0.813-0.833l-0.938-0.272l-0.851,0.631l-0.67,0.614l-1.083,0.106l-0.904,0.09l-0.108,0.741l0.288,1.068l0.722-0.073l-0.651,0.795l-0.129,0.559l-1.049,0.47l-0.757-0.291l-0.433-0.688l-0.651,0.794l-0.651,0.795l-0.309,0.578l-0.688,0.433l-0.47-1.049l-0.069-0.723l-0.435-0.688l-0.415-0.507l-0.631-0.85l-1.121-0.254l-1.643-0.021l-0.577-0.309l-0.761-0.29l-0.722,0.071l-0.235-0.524l-0.903,0.089l-1.41,0.504l-1.3-0.237l-1.321-0.416l-0.541,0.053L250,132.249l-1.104-0.073l-0.073,1.102l-0.722,0.072l0.053,0.543l-0.869,0.449l-53.113-0.052l-0.002,0.043v45.292l0.08-0.038l1.109-0.168l1.834,0.86l1.024-0.723l1.748,0.305l2.12,0.248l1.73,1.44l0.492,2.009l1.092,0.971l0.045-0.953l1.055-0.539l0.98,0.232l1.721,0.119l1.008,0.413l0.604,2.748l1.444,2.054l1.138,0.018l1.619,0.701l1.973,1.783l0.379,1.268l1.277,0.943l1.619,0.701l1.295-0.195l-0.223-1.481l0.471-0.638l0.741-0.11l0.823,0.444l1.85-0.28l1.434,0.729l0.925-0.139l1.223,0.571l1.164,0.204l0.658-0.666l0.896-0.327l1.037,0.603l1.961,0.461l1.451-0.408l1.083-0.354l0.74-0.111l0.711-0.295l0.899-0.326l1.433,0.73l-0.204,1.168l0.566,1.235l0.722,1.028l0.354,1.082l-0.178,1.349l8.182,4.065l1.721,0.121l0.873,0.643h0.513l-0.213,0.64l0.112-0.336l0.227,0.167l0.939-0.471l-0.213-1.704l0.427-0.212h0.425l-0.425-1.065l-0.853-0.213l0.426-0.853l-0.426-1.064l0.426,0.214l0.427-1.491l0.851-3.406l-0.213-2.131l0.426-1.277h-0.426l1.065-0.852l-0.64-0.853l0.854,0.213l1.703-4.046l1.49-0.428l-0.641-1.275l0.641-0.214v0.853l0.424-0.214l-0.424-1.276l-0.426,0.213l0.213-0.426l-0.854-0.213l1.49-0.64l0.427-1.491l-0.427-0.639l0.64-0.215v-1.489l1.703-1.703l-0.638-0.214l1.063-0.213l-1.276-0.426l1.489-0.213l0.214-1.064l-0.64,0.426l-0.427-0.426l0.64,0.213l-0.213-0.639l0.64,0.426l0.213-1.704v-0.212l-0.427,0.425v-0.639l-0.213,0.214l-0.213-0.641l0.64,0.427l0.213-1.064v0.853l0.852-0.426l0.214-1.064l-0.427-0.427h0.854l0.637-1.703l-0.637,0.853l-0.214-0.853h0.638v-0.853l0.213,0.853l0.854-1.491l-0.213-0.426h0.427v0.64l2.556-1.491l-0.853-0.213l-0.853,0.639l-0.213-0.213l0.426-0.426l-0.213-0.426l0.853,0.426l0.638-0.426l0.215,0.426l0.853-1.277l1.489-0.853l0.214-1.702l-0.64-0.215v0.428l-0.852-0.428h1.064l0.213-1.49l1.49-1.277l1.918-6.176l-0.213-4.26l1.489-3.834l0.213-0.639l0.64-3.62l-0.64-0.426l0.64,0.213l-0.213-0.853l1.703-3.193h-0.426l0.426-0.214L278.939,132.632z M261.268,143.072h-0.215l-0.213-0.639l0.641-0.214L261.268,143.072z"
    icons.append(icon1)
    icon2 = "M112.615,33.818l-0.426-0.425l-0.852-0.213l-1.278,0.213l0.852,0.639l0.213,0.852l-0.852-1.065l0.638,1.065l-0.212-0.213l-0.213,0.426l-0.426-0.426l-0.213,0.852l-0.426-1.064l-0.426,0.639l1.064,2.982h-0.426l-0.213-1.065l-1.065-1.065v1.704l-0.639,0.639l0.426-0.852l-0.426-0.639l0.426-0.213l-0.213-1.277l0.639-1.491h-0.426l0.852-0.212l-0.426-0.639l0.426-0.212l-1.491-1.065l-0.212,0.425l-1.917-2.981l-1.491-0.852l-0.213-0.852l-0.639-0.213l0.213,0.638l-0.639-0.638l-0.426,0.425V27.22l-0.426,0.425l-0.426-1.064l-1.278-0.427v0.427l-0.852-0.213l0.426,1.065l0.852,0.425l-0.373-0.053l-1.118-0.16l0.213,0.64L98.77,28.71l-0.213-0.425l-0.213,1.277l-0.639-1.277l-0.426,0.212l0.426-1.064l-1.277,0.852l-0.213,0.425l0.426,0.426l-0.852,0.426l-0.213-1.065H95.15l0.426-0.425H95.15l0.426-0.426l-0.639,0.426l-0.639-0.213v0.427l-0.213-0.427v0.427l1.278,0.639l-0.852,0.639l0.213,0.638l-0.639,0.427l0.426,0.852h-0.852v1.065l-0.639-0.639l0.212-0.853l-0.852,0.213v-0.639l-0.639,1.704l0.213-1.917l0.426-0.639l-0.852-0.426v2.343l-0.639-0.213l-0.426,0.852l-0.213-0.639l-0.426,0.425l0.213-0.852l-0.852,0.852l0.426,0.213l-1.278,0.639l0.639,0.853h0.639l-0.852,0.64l1.278,0.425l0.213-0.425l0.426,0.212l-0.852,0.852l1.064,0.426h-1.064l-0.426-0.639l-0.852,0.639l-0.639-1.49l-0.426,0.212l0.213,0.852l-1.278,0.213l0.426,0.213l-0.213,0.639l1.278-0.852l-1.278,1.065l0.426,0.426l1.065-0.64v0.426h0.426l-0.639,0.639l1.277,1.064l-1.064-0.852l-0.426,0.425l-0.426-0.852l-0.852-0.212v-0.426l-0.639,0.426l-0.426,0.852l-0.213-0.427l-0.212,0.639l-0.852-0.212l0.213,0.212l-0.852,0.64l0.426,0.212l-0.639,0.213l0.852,2.342l0.213-0.372v0.16l0.426-0.64l-0.355,0.355l0.568-0.994l0.639-0.425l-0.426,0.425h0.639l-0.852,0.639l-0.213,1.491h0.426l-0.852,0.425l0.426,0.213l-0.426,0.213l-0.426-1.065l-0.426,1.917l1.491-0.213l1.278,0.639l1.065-0.212l-1.065,0.425l-0.426-0.425l-1.917,0.212l-0.426-0.426l-0.426,0.426l0.373,0.224l-1.011,0.203l0.639-0.213l-0.639-0.213l-0.639-0.852l-1.491-0.639l0.639,0.639h-0.426l0.426,0.64l-0.852-0.64v0.213l-1.065-0.426h0.426l-0.212-0.426h0.426l-0.852-0.425v0.425l-0.639-0.213l0.213,0.427l-0.426-0.427l0.426,0.64l-0.426,0.212l0.852,0.213l0.212,0.426l-0.639-0.213l0.639,0.426H77.48l1.064,0.639h-1.49l0.426,0.639l0.212-0.426l0.639,0.213l-0.852,0.639l1.49,0.426l0.426,1.278l0.852-0.426v-0.426l0.426,0.213l-1.064,1.065l0.426,0.426l-0.639-0.213l1.065,1.917l-1.917-1.917l-0.639,0.213l0.852,1.49l-0.426-0.213l-0.426,1.065v1.065l-1.278-1.278l-0.639-2.129l-0.852-0.64v-1.704h-0.639l-0.639-0.639l0.213-0.852l0.639-0.213l-0.426-0.639l-0.639,0.213l-1.278,2.129l0.639,0.639l-1.704-0.212l-0.213,0.639l0.426,0.852l-0.852-0.426v0.426l-0.852,0.213l-0.639,0.852l0.426,0.213l-1.065,0.852l-0.213,1.916l0.639,1.491l-0.426,1.491l1.491,0.213v0.852l-2.981,2.13l-0.852,0.212l-0.639,0.852l0.426,0.64l-1.065,0.212l0.213,0.852l-1.065,1.917l-2.555,3.195l-5.963,2.556l-1.491,0.213h-1.491L51.924,69.6l-0.852,0.639L50.434,69.6l-1.917-0.426L48.73,69.6v0.213L48.517,69.6l-0.426-0.213L47.878,69.6l-1.491,1.917l-4.472,0.852v-0.426l-1.704,1.065l0.213,0.426h-0.639l-0.426,0.852l-1.065,0.213v-0.213l-1.704,0.852l-1.278-0.639l-0.213-0.64l-1.491,0.852l-0.639-0.212l-0.426-0.213l0.639-1.065h-0.426l-1.065,1.278l0.212,0.212h-0.426l-2.129,1.065l-0.639-0.426l-0.213,1.064l-1.704,0.852l-0.639,1.278l-1.064,0.213l-1.065,1.704l-4.046,1.065l-1.704,1.064l-0.213,1.278l-0.426,0.213l-0.426-0.213l0.213,0.852l-0.639,1.065l0.426,0.426l-0.426-0.212l0.212,0.425l-0.852,1.065l-0.426-0.639l-1.065,0.639l0.426-1.49l-0.426,0.425l-0.213-1.49l0.852-2.556L13.8,82.804l-2.129,5.111l1.065,2.769l-0.426,1.278l0.213,2.555l-2.129,2.982l-0.426,3.833l1.704,2.769l-0.213,0.427l0.426,1.704l0.852,0.639l2.342,4.685l0.639,0.213l0.212,1.064h-0.639l0.213,2.343l-1.064,1.277l-1.065-1.704l-0.213-2.342v1.065l-1.065,0.852l0.213-2.343l-1.704-2.769l-0.639,1.704l0.426,0.426v-0.852l0.639,3.194l2.13,1.704l-0.213,1.917l-1.277,0.64l-0.213-1.491l-0.213,1.278l-0.426-2.556l-0.213,1.277l-0.852-3.407l0.213,2.769l-0.639-0.426v-2.342l-0.213,1.704l-0.852-0.639l5.537,8.093l1.278,3.407l-0.426,1.065l0.426,2.129l2.343,2.769l0.639,1.278l-0.213,0.852l1.917,2.557l0.852,2.98l-0.213,3.833v0.427l0.639,3.407l4.259,8.944l0.213,3.193l1.065-0.639v0.425l-1.065,0.214l0.213,1.064l-0.426,0.639l0.213,1.491l-0.852,1.704l0.639,4.896l-2.342,2.77h-1.065l-1.278-0.853v4.474l0.852,2.342l0.212-0.426l1.278-0.213l2.342,1.277l1.917,2.98l2.555,0.853l0.213-0.639l0.852,0.639h-1.065l1.704,1.063l0.639-0.639l1.278,0.639l2.981-0.424l1.704,1.062l0.426-0.852l1.917,0.64l0.426-0.213l-1.064-0.427l0.426-0.853l0.426-0.213l-0.213,0.853h1.704l-0.213-0.64l1.491-0.213l0.213-1.278l1.917-0.852l0.212-0.852l1.065-0.428l-0.426-0.425l2.769,0.853l0.213-0.853l0.852,0.213v-0.853l1.065,0.213l-0.852-0.853l2.981-2.769h0.639l2.768,0.426l1.065-0.852l5.324-0.64l2.769,0.853l1.49-0.639l0.852,1.49h1.065l0.426-0.854l1.491,0.427l0.212-0.64l2.769-0.213l0.639,0.426l0.213,0.854l1.491-1.064l1.064,0.426l2.982-2.981l0.852-3.407l0.852-0.852l3.833-1.278l7.667-4.472l1.704-0.426l3.195,0.426l3.62-0.214l6.814-2.129l4.642-2.321V44.302l-0.381,0.381l-0.427-0.213v1.704l-0.638,0.851v-0.212l0.213-0.426l-1.278-0.426l0.213-0.852l-0.639,0.426l0.852-1.491l-0.213-0.638h0.638l-0.425-0.64l1.065-0.638l-0.426,0.638l0.426,0.213l0.852-0.638l0.168,0.042v-8.565H112.615z M83.443,45.535v-0.81l0.639,0.384L83.443,45.535z M113.852,44.081V43.35l-0.168,0.056L113.852,44.081z"
    icons.append(icon2)
    args = {
            'icons': json.dumps(icons),
            }
    return render(request, 'index.html', args)
