from django.conf.urls import url
from cmoapp.views import ChiefOfficerManager

urlpatterns = [
    url(r'^$', ChiefOfficerManager.index, name="Chief_Index"),
    url(r'^action_plans/(?P<pk>\d+)/$', ChiefOfficerManager.ActionPlanDetail.as_view(), name='Chief_Action_Plan_Detail'),
    url(r'^approve_action_plan/$', ChiefOfficerManager.ApproveActionPlan, name="Approve_Action_Plan"),
    url(r'^reject_action_plan/$', ChiefOfficerManager.RejectActionPlan, name="Reject_Action_Plan"),
    url(r'^reload_data/$', ChiefOfficerManager.ReloadData, name="Reload_Data"),
    url(r'^select_crisischat/$', ChiefOfficerManager.select_crisischat, name="Select_Crisischat"),

]