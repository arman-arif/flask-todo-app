from app.controllers import TaskController
from app.routes.route import Route

Route.get('/', TaskController.index)
Route.get('/task-list', TaskController.list)
Route.post('/add-task', TaskController.add)
# route.post('/update/<int:task_id>', TaskController.toggle_done)
Route.delete('/delete-task/<int:task_id>', TaskController.delete)
