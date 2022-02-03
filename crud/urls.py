from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^pengguna$', views.users, name='pengguna'),
    url(r'^jenis_simpanan$', views.jenis_simpanan, name='jenis_simpanan'),
    url(r'^data_kas$', views.data_kas, name='data_kas'),
    url(r'^create$', views.create, name='create'),
    url(r'^keanggotaan$', views.keanggotaan, name='keanggotaan'),
    url(r'^keanggotaan/edit/(?P<id>\d+)$', views.editkeanggotaan, name='editkeanggotaan'),
    url(r'^keanggotaan/edit/updatekeanggotaan/(?P<id>\d+)$', views.updatekeanggotaan, name='updatekeanggotaan'),
    url(r'^keanggotaan/delete/(?P<id>\d+)$', views.deleteKeanggotaan, name='deleteKeanggotaan'),
    url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^list$', views.list, name='list'),
    url(r'^anggota$', views.anggota, name='anggota'),
    url(r'^fileupload$', views.fileupload, name='fileupload'),
    url(r'^keanggotaan/tambah$', views.tambah_anggota, name='tambah_anggota'),
    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),

    url(r'^ajax/$', views.ajax, name='ajax'),
    url(r'^ajax/ajax$', views.ajax, name='ajaxpost'),
    url(r'^ajax/delete$', views.ajax_delete, name='ajax_delete'),
    url(r'^ajax/getajax$', views.getajax, name='getajax'),
    url(r'^register/$', views.register,name='register'),
    url(r'^register/success/$',views.register_success,name='register_success'),
    url(r'^users/$',views.users,name='users'),
    url(r'^users/delete/(?P<id>\d+)$', views.user_delete, name='user_delete'),
    url(r'^upload/csv/$', views.upload_csv, name='upload_csv'),
    url(r'^change_password$', views.changePassword, name='changePassword'),
    url(r'^file/delete$', views.changePassword, name='changePassword'),
    url(r'^file/delete/(?P<id>\d+)$', views.deleteFiles, name='deleteFiles'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)