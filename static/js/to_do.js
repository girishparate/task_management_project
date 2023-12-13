function task_delete(task_id){
    $.ajax({
        type: 'delete',
        headers: {
            'X-CSRFToken': csrftoken
        },
        url: `/task/task-delete-edit/`+task_id,
        success: function(response) {
            var data = window.location.origin
            window.location.href = '/task/task-dashboard';
        },
        error: function(response) {
        }
    })
}

function task_edit(task_id){

    var title = $('#edit-title').val()
    var description = $('#edit-description').val()
    var status = $('#edit-status').val()

    data = {
        'title':title,
        'description':description,
        'status':status,
        
     }
    
    $.ajax({
        type: 'put',
        headers: {
            'X-CSRFToken': csrftoken
        },
        enctype: "multipart/form-data",
        data: data,
        url: `/task/task-delete-edit/`+task_id,
        success: function(response) {

            var data = window.location.origin + '/task-details/' + response.slug
            window.location.href = '/task/task-dashboard';
        },
        error: function(response) {
        }
    })
}