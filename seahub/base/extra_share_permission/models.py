# Copyright (c) 2012-2016 Seafile Ltd.

from django.db import models


class ExtraSharePermissionManager(models.Manager):
    def get_user_permission(self, repo_id, username):
        record_list = super(ExtraSharePermissionManager, self).filter(
            repo_id=repo_id, share_to=username
        )
        if len(record_list) > 0:
            return record_list[0].permission
        else:
            return None

    def get_shared_repos_by_shared_with_admin(self, username):
        shared_repos = super(ExtraSharePermissionManager, self).filter(
            share_to=username, permission='admin'
        )
        return [e.repo_id for e in shared_repos]

    def get_shared_repos_by_shared_with_preview(self, username):
        shared_repos = super(ExtraSharePermissionManager, self).filter(
            share_to=username, permission='preview'
        )
        return [e.repo_id for e in shared_repos]

    def get_permission_by_owner_shared(self, repo_id, username):
        shared_repos = super(ExtraSharePermissionManager, self).filter(
            repo_id=repo_id
        )
        shared_repos = [(e.share_to, e.permission) for e in shared_repos]
        return shared_repos

    def create_share_permission(self, repo_id, username, permission):
        self.model(repo_id=repo_id,  share_to=username, 
                   permission=permission).save()

    def delete_user_shared_repo(self, repo_id,  share_to):
        super(ExtraSharePermissionManager, self).filter(repo_id=repo_id, 
                                                   share_to=share_to).delete()

    def update_share_permission(self, repo_id, share_to, permission):
        super(ExtraSharePermissionManager, self).filter(repo_id=repo_id, 
                                                   share_to=share_to).delete()
        if permission in ['admin', 'preview']:
            self.create_share_permission(repo_id, share_to, permission)


class ExtraSharePermission(models.Model):
    repo_id = models.CharField(max_length=36, db_index=True)
    share_to = models.CharField(max_length=255, db_index=True)
    permission = models.CharField(max_length=30)
    objects = ExtraSharePermissionManager()
