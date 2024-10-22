from django.urls import path
from apps.homeworkflow.views import HomeworkApiView, AbsenceApiView, HomeworkMissingView, WeeklyFeedbackApiView

app_name ='homeworkflow-urls'
urlpatterns = [
    path("homework/", HomeworkApiView.as_view(), name='all-homework'),
    path("absence/", AbsenceApiView.as_view(), name='post-absence'),
    path("homework/uncompleted/", HomeworkMissingView.as_view(), name="missing-homework"),
    path("weeklyfeedback/", WeeklyFeedbackApiView.as_view(), name='create-weeklyfeedback'),
    path("weeklyfeedback/<int:id>/", WeeklyFeedbackApiView.as_view(), name='create-weeklyfeedback')
]