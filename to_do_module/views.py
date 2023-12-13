from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .serializers import Task, TaskSerializers
from django.db import transaction
from django.shortcuts import render
# Create your views here.


class TaskDashboardView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'task_dashboard.html'

    """
    get method to display all the tasks in the html page
    """
    @transaction.atomic()
    def get(self, request):
        tasks = Task.objects.filter(user=request.user)
        tasks = TaskSerializers(tasks, many=True).data
        data = {'tasks': tasks}
        return Response(data)
    

    """
    post method to save the task data
    """
    @transaction.atomic()
    def post(self, request):
        data = {}
        serializer = TaskSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            data['message'] = 'Task Saved successfully.'
        else:
            data['message'] = 'Cannot save task.'
        return Response(data)
    

class TaskCRUDView(APIView):
    def get_object(self, pk):
        return Task.objects.get(pk=pk)
    
    def get(self, request, pk):
        task = self.get_object(pk)
        data = {'task': TaskSerializers(task).data}

        return render(request, 'task_detail.html', data)
    
    def put(self, request, pk):
        data = {}
        task = self.get_object(pk)
        task = TaskSerializers(instance=task, data=request.data)
        if task.is_valid():
            task.save()
            data['messages'] = 'Task updated successfully.'
        else:
            data['messages'] = 'Cannot update task.'
        return Response(data)

    def delete(self, request, pk):
        data = {}
        task = self.get_object(pk)
        task.delete()
        data['message'] = 'Task deleted successfully.'
        return Response(data)