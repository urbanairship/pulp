from django.conf.urls import patterns, url

from pulp.server.webservices.views.consumer_groups import (ConsumerGroupAssociateActionView,
                                                           ConsumerGroupBindingView,
                                                           ConsumerGroupBindingsView,
                                                           ConsumerGroupContentActionView,
                                                           ConsumerGroupResourceView,
                                                           ConsumerGroupUnassociateActionView,
                                                           ConsumerGroupView)
from pulp.server.webservices.views.content import (
    CatalogResourceView, ContentTypeResourceView, ContentTypesView, ContentUnitResourceView,
    ContentUnitsCollectionView,ContentUnitUserMetadataResourceView,
    DeleteOrphansActionView, OrphanCollectionView, OrphanResourceView,
    OrphanTypeSubCollectionView, UploadsCollectionView, UploadResourceView,
    UploadSegmentResourceView
)
from pulp.server.webservices.views.dispatch import TaskCollectionView, TaskResourceView
from pulp.server.webservices.views.events import (EventResourceView, EventView)
from pulp.server.webservices.views.permissions import (GrantToRoleView, GrantToUserView,
                                                       PermissionView, RevokeFromRoleView,
                                                       RevokeFromUserView)
from pulp.server.webservices.views.plugins import (DistributorResourceView, DistributorsView,
                                                   ImporterResourceView, ImportersView,
                                                   TypeResourceView, TypesView)
from pulp.server.webservices.views.repo_groups import (
    RepoGroupAssociateView, RepoGroupDistributorResourceView, RepoGroupDistributorsView,
    RepoGroupPublishView, RepoGroupResourceView, RepoGroupsView, RepoGroupUnassociateView
)
from pulp.server.webservices.views.roles import (RoleResourceView, RoleUserView, RoleUsersView,
                                                 RolesView)
from pulp.server.webservices.views.root_actions import LoginView
from pulp.server.webservices.views.status import StatusView
from pulp.server.webservices.views.users import UserResourceView, UsersView


urlpatterns = patterns('',
    url(r'^v2/actions/login/$', LoginView.as_view(), name='login'), # flake8: noqa
    url(r'^v2/consumer_groups/$', ConsumerGroupView.as_view(), name='consumer_group'),
    url(r'^v2/consumer_groups/(?P<consumer_group_id>[^/]+)/$',
        ConsumerGroupResourceView.as_view(), name='consumer_group_resource'),
    url(r'^v2/consumer_groups/(?P<consumer_group_id>[^/]+)/actions/associate/$',
        ConsumerGroupAssociateActionView.as_view(), name='consumer_group_associate'),
    url(r'^v2/consumer_groups/(?P<consumer_group_id>[^/]+)/actions/unassociate/$',
        ConsumerGroupUnassociateActionView.as_view(), name='consumer_group_unassociate'),
    url(r'^v2/consumer_groups/(?P<consumer_group_id>[^/]+)/actions/content/(?P<action>[^/]+)/$',
        ConsumerGroupContentActionView.as_view(), name='consumer_group_content'),
    url(r'^v2/consumer_groups/(?P<consumer_group_id>[^/]+)/bindings/$',
        ConsumerGroupBindingsView.as_view(), name='consumer_group_bind'),
    url(r'^v2/consumer_groups/(?P<consumer_group_id>[^/]+)' +
        r'/bindings/(?P<repo_id>[^/]+)/(?P<distributor_id>[^/]+)/$',
        ConsumerGroupBindingView.as_view(), name='consumer_group_unbind'),
    url(r'^v2/content/actions/delete_orphans/$', DeleteOrphansActionView.as_view(),
        name='content_actions_delete_orphans'),
    url(r'^v2/content/catalog/(?P<source_id>[^/]+)/$', CatalogResourceView.as_view(),
        name='content_catalog_resource'),
    url(r'^v2/content/orphans/$', OrphanCollectionView.as_view(), name='content_orphan_collection'),
    url(r'^v2/content/orphans/(?P<content_type>[^/]+)/$', OrphanTypeSubCollectionView.as_view(),
        name='content_orphan_type_subcollection'),
    url(r'^v2/content/orphans/(?P<content_type>[^/]+)/(?P<unit_id>[^/]+)/$',
        OrphanResourceView.as_view(), name='content_orphan_resource'),
    url(r'^v2/content/types/$', ContentTypesView.as_view(),
        name='content_types'),
    url(r'^v2/content/types/(?P<type_id>[^/]+)/$', ContentTypeResourceView.as_view(),
        name='content_type_resource'),
    url(r'^v2/content/units/(?P<type_id>[^/]+)/$', ContentUnitsCollectionView.as_view(),
        name='content_units_collection'),
    url(r'^v2/content/units/(?P<type_id>[^/]+)/(?P<unit_id>[^/]+)/$',
        ContentUnitResourceView.as_view(), name='content_unit_resource'),
    url(r'^v2/content/units/(?P<type_id>[^/]+)/(?P<unit_id>[^/]+)/pulp_user_metadata/$',
        ContentUnitUserMetadataResourceView.as_view(), name='content_unit_user_metadata_resource'),
    url(r'^v2/content/uploads/$', UploadsCollectionView.as_view(), name='content_uploads'),
    url(r'^v2/content/uploads/(?P<upload_id>[^/]+)/$', UploadResourceView.as_view(),
        name='content_upload_resource'),
    url(r'^v2/content/uploads/(?P<upload_id>[^/]+)/(?P<offset>[^/]+)/$',
        UploadSegmentResourceView.as_view(), name='content_upload_segment_resource'),
    url(r'^v2/events/$', EventView.as_view(), name='events'),
    url(r'^v2/events/(?P<event_listener_id>[^/]+)/$', EventResourceView.as_view(), name='event_resource'),
    url(r'^v2/permissions/$', PermissionView.as_view(), name='permissions'),
    url(r'^v2/permissions/actions/grant_to_role/$', GrantToRoleView.as_view(), name='grant_to_role'),
    url(r'^v2/permissions/actions/grant_to_user/$', GrantToUserView.as_view(), name='grant_to_user'),
    url(r'^v2/permissions/actions/revoke_from_role/$', RevokeFromRoleView.as_view(), name='revoke_from_role'),
    url(r'^v2/permissions/actions/revoke_from_user/$', RevokeFromUserView.as_view(), name='revoke_from_user'),
    url(r'^v2/plugins/distributors/$', DistributorsView.as_view(), name='plugin_distributors'),
    url(r'^v2/plugins/distributors/(?P<distributor_id>[^/]+)/$', DistributorResourceView.as_view(),
        name='plugin_distributor_resource'),
    url(r'^v2/plugins/importers/$', ImportersView.as_view(), name='plugin_importers'),
    url(r'^v2/plugins/importers/(?P<importer_id>[^/]+)/$', ImporterResourceView.as_view(),
        name='plugin_importer_resource'),
    url(r'^v2/plugins/types/$', TypesView.as_view(), name='plugin_types'),
    url(r'^v2/plugins/types/(?P<type_id>[^/]+)/$', TypeResourceView.as_view(),
        name='plugin_type_resource'),
    url(r'^v2/repo_groups/$', RepoGroupsView.as_view(), name='repo_groups'),
    url(r'^v2/repo_groups/(?P<repo_group_id>[^/]+)/$', RepoGroupResourceView.as_view(),
        name='repo_group_resource'),
    url(r'^v2/repo_groups/(?P<repo_group_id>[^/]+)/actions/associate/$',
        RepoGroupAssociateView.as_view(), name='repo_group_associate'),
    url(r'^v2/repo_groups/(?P<repo_group_id>[^/]+)/actions/publish/$',
        RepoGroupPublishView.as_view(), name='repo_group_publish'),
    url(r'^v2/repo_groups/(?P<repo_group_id>[^/]+)/actions/unassociate/$',
        RepoGroupUnassociateView.as_view(), name='repo_group_unassociate'),
    url(r'^v2/repo_groups/(?P<repo_group_id>[^/]+)/distributors/$',
        RepoGroupDistributorsView.as_view(), name='repo_group_distributors'),
    url(r'^v2/repo_groups/(?P<repo_group_id>[^/]+)/distributors/(?P<distributor_id>[^/]+)/$',
        RepoGroupDistributorResourceView.as_view(), name='repo_group_distributor_resource'),
    url(r'^v2/roles/$', RolesView.as_view(), name='roles'),
    url(r'^v2/roles/(?P<role_id>[^/]+)/$', RoleResourceView.as_view(), name='role_resource'),
    url(r'^v2/roles/(?P<role_id>[^/]+)/users/$', RoleUsersView.as_view(), name='role_users'),
    url(r'^v2/roles/(?P<role_id>[^/]+)/users/(?P<login>[^/]+)/$', RoleUserView.as_view(), name='role_user'),
    url(r'^v2/status/$', StatusView.as_view(), name='status'),
    url(r'^v2/tasks/$', TaskCollectionView.as_view(), name='task_collection'),
    url(r'^v2/tasks/(?P<task_id>[^/]+)/$', TaskResourceView.as_view(), name='task_resource'),
    url(r'^v2/users/$', UsersView.as_view(), name='users'),
    url(r'^v2/users/(?P<login>[^/]+)/$', UserResourceView.as_view(), name='user_resource')
)
