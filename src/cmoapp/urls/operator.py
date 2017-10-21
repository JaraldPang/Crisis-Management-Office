from django.conf.urls import url
from cmoapp.views import OperatorManager

urlpatterns = [
    url(r'^(?P<pk>\d+)', OperatorManager.assignnewCrisis, name='Operator_AssignCrisis'),

    url(r'^allolist/$', OperatorManager.getCrisisAllocationList, name='Operator_ViewAllocationList'),
    url(r'^alloexcrisis/$', OperatorManager.allocateToExistingCrisis, name='Operator_allocateToExistingCrisis'),
    url(r'^allocrisis/$', OperatorManager.allocateCrisis, name='Operator_AllocateCrisis'),
    url(r'^newcrisisrpt/$', OperatorManager.newCrisisReport, name='Operator_NewCrisisReport'),

   #url(r'^(?P<pk>[0-9]+)/', OperatorManager.viewCrisis, name = "View_Crisis"),
    url(r'^$', OperatorManager.index, name="Operator_Index"),
    url(r'^create_crisis/$', OperatorManager.create_crisis, name="create_crisis"),
    url(r'^delete_crisis/$', OperatorManager.delete_crisis, name="delete_crisis")
]