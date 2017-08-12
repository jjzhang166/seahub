from seahub.base.extra_share_permission.models import ExtraSharePermission
from seahub.test_utils import BaseTestCase


class ExtraSharePermissionTest(BaseTestCase):
    def test_can_add(self):
        ExtraSharePermission.objects.create_share_permission(self.repo.id, 
                                                             self.user.username, 
                                                             'admin')
        self.assertEqual(1, len(ExtraSharePermission.objects.all()))

    def test_can_update(self):
        ExtraSharePermission.objects.create_share_permission(self.repo.id, 
                                                             self.user.username, 
                                                             'admin')
        ExtraSharePermission.objects.update_share_permission(self.repo.id, 
                                                            self.user.username, 
                                                            'preview')
        self.assertEqual('preview', ExtraSharePermission.objects.all()[0].permission)

    def test_can_delete(self):
        ExtraSharePermission.objects.create_share_permission(self.repo.id, 
                                                             self.user.username, 
                                                             'admin')
        ExtraSharePermission.objects.delete_user_shared_repo(self.repo.id, 
                                                             self.user.username)
        self.assertEqual(0, len(ExtraSharePermission.objects.all()))

    def test_can_get_user_permission(self):
        self.assertEqual(None, ExtraSharePermission.objects.\
                         get_user_permission(self.repo.id, self.user.username))
        ExtraSharePermission.objects.create_share_permission(self.repo.id, 
                                                             self.user.username, 
                                                             'admin')
        self.assertEqual('admin', ExtraSharePermission.objects.\
                         get_user_permission(self.repo.id, self.user.username))

    def test_can_get_shared_repos_with_admin(self):
        self.assertEqual([], ExtraSharePermission.objects.\
                        get_shared_repos_by_shared_with_admin(self.user.username))
        ExtraSharePermission.objects.create_share_permission(self.repo.id, 
                                                             self.user.username, 
                                                             'admin')
        self.assertEqual([self.repo.id], ExtraSharePermission.objects.\
                        get_shared_repos_by_shared_with_admin(self.user.username))

    def test_can_get_shared_repos_with_preview(self):
        self.assertEqual([], ExtraSharePermission.objects.\
                        get_shared_repos_by_shared_with_preview(self.user.username))
        ExtraSharePermission.objects.create_share_permission(self.repo.id, 
                                                             self.user.username, 
                                                             'preview')
        self.assertEqual([self.repo.id], ExtraSharePermission.objects.\
                        get_shared_repos_by_shared_with_preview(self.user.username))

    def test_get_permission_by_owner_shared(self):
        self.assertEqual([], ExtraSharePermission.objects.\
                        get_permission_by_owner_shared(self.repo.id))
        ExtraSharePermission.objects.create_share_permission(self.repo.id, 
                                                             self.user.username, 
                                                             'admin')
        self.assertEqual([(self.user.username, 'admin')], ExtraSharePermission.objects.\
                        get_permission_by_owner_shared(self.repo.id))
