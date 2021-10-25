from django.db import models


class ActionPermission(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False, unique=True)
    active_ind = models.BooleanField(blank=False, null=True, default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Action Permission'
        verbose_name_plural = 'Action Permissions'


class GroupActionPermission(models.Model):
    group = models.ForeignKey("auth.Group", null=True, blank=False, on_delete=models.CASCADE)
    permission = models.ForeignKey(ActionPermission, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.group.name}.{self.permission.name}"

    class Meta:
        verbose_name = 'Group Action Permission'
        verbose_name_plural = 'Group Action Permissions'
        constraints = [
            models.UniqueConstraint(fields=['group', 'permission'], name='groupactionpermission_permission')
        ]


class UserActionPermission(models.Model):
    user = models.ForeignKey("auth.User", null=True, blank=False, on_delete=models.CASCADE)
    permission = models.ForeignKey(ActionPermission, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}.{self.permission.name}"

    class Meta:
        verbose_name = 'User Action Permission'
        verbose_name_plural = 'User Action Permissions'
        constraints = [
            models.UniqueConstraint(fields=['user', 'permission'], name='useractionpermission_permission')
        ]
