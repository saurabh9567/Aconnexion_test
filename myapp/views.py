from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
import codecs

#GET API to read files from text_files folder and will return response to browser
@api_view(['GET'])
def read_file_text(request):
    try:
        file = request.GET.get('file', 'file1') #Get file name from query parameters
        start = int(request.GET.get('start', 0)) #Get Start line number from query parameters
        end = int(request.GET.get('end', -1)) #Get End line number from query parameters
        file_name = 'myapp\\text_files\\file_name.txt'.replace('file_name', file) #set file path
        encodings = ['utf-8', 'utf-16'] #encodings list
        for e in encodings:
            try:
                f = codecs.open(file_name, 'r', encoding=e)
                file_data = f.readlines()
                if(end == -1): 
                    end = len(file_data) #get end line number i.e. length from file
                file_data = ''.join(file_data[start:end+1]) #convert list to string
            except UnicodeDecodeError as ude:
                exception_detail = ude 
            else:
                print('opening the file with encoding:  %s ' % e)
                exception_detail = '' 
                break    
        if exception_detail == '': #if there is no exception
            return render(request, 'myapp/mytemplate.html', {'output_data': file_data})
        else: #if there is UnicodeDecodeError exception
            return render(request, 'myapp/mytemplate.html', {'output_data': exception_detail})
    except Exception as ex: #if any other exception 
        exception_detail = ex
        return render(request, 'myapp/mytemplate.html', {'output_data': exception_detail})