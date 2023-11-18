from django.db import models

# Create your models here.
from django_tenants.models import TenantMixin

class EnterpriseTenant(TenantMixin):
    tenant_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    # 添加其他租户字段

    auto_create_schema = True  # 自动创建数据库模式

    def __str__(self):
        return self.tenant_number
