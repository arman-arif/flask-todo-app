from app.controllers import TaskController
from app.routes.route import Route

Route.get('/', TaskController.index)
Route.post('/add-task', TaskController.add)
# route.post('/update/<int:task_id>', TaskController.toggle_done)
# route.post('/delete/<int:task_id>', TaskController.delete)
