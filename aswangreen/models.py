# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DataentryArea(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    created_at_date = models.DateField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_at_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    counter = models.IntegerField(blank=True, null=True)
    is_test = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'DataEntry_area'


class DataentryClient(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    created_at_date = models.DateField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_at_date = models.DateField(blank=True, null=True)
    serialnum = models.IntegerField(db_column='serialNum', unique=True, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    password = models.CharField(max_length=150, blank=True, null=True)
    nationalid = models.CharField(db_column='nationalId', max_length=14, blank=True, null=True)  # Field name made lowercase.
    streetname = models.CharField(db_column='streetName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    addressbuilding = models.CharField(db_column='addressBuilding', max_length=150, blank=True, null=True)  # Field name made lowercase.
    addressapartment = models.CharField(db_column='addressApartment', max_length=150, blank=True, null=True)  # Field name made lowercase.
    addressdetails = models.TextField(db_column='addressDetails', blank=True, null=True)  # Field name made lowercase.
    created_prev_date = models.DateField(blank=True, null=True)
    activation_request = models.IntegerField()
    outsource = models.IntegerField()
    is_employee = models.IntegerField()
    missing_info = models.IntegerField()
    activation_request_accepted = models.IntegerField()
    is_test = models.IntegerField()
    contactme = models.CharField(db_column='contactMe', max_length=50, blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    deserved = models.IntegerField()
    area = models.ForeignKey(DataentryArea, models.DO_NOTHING, blank=True, null=True)
    belongs_to = models.ForeignKey('DataentryEmployee', models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('DataentryEmployee', models.DO_NOTHING, blank=True, null=True)
    modified_by = models.ForeignKey('DataentryEmployee', models.DO_NOTHING, blank=True, null=True)
    contractdate = models.DateField(db_column='contractDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DataEntry_client'


class DataentryCollectorder(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    created_at_date = models.DateField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_at_date = models.DateField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    confirmed = models.IntegerField()
    reason = models.CharField(max_length=100, blank=True, null=True)
    required = models.IntegerField()
    created_prev_date = models.DateField(blank=True, null=True)
    is_test = models.IntegerField()
    collector = models.ForeignKey('DataentryEmployee', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DataEntry_collectorder'


class DataentryCollectorderAreas(models.Model):
    id = models.BigAutoField(primary_key=True)
    collectorder = models.ForeignKey(DataentryCollectorder, models.DO_NOTHING)
    area = models.ForeignKey(DataentryArea, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'DataEntry_collectorder_areas'
        unique_together = (('collectorder', 'area'),)


class DataentryCollectorderClients(models.Model):
    id = models.BigAutoField(primary_key=True)
    collectorder = models.ForeignKey(DataentryCollectorder, models.DO_NOTHING)
    client = models.ForeignKey(DataentryClient, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'DataEntry_collectorder_clients'
        unique_together = (('collectorder', 'client'),)


class DataentryContactrequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    created_at_date = models.DateField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_at_date = models.DateField(blank=True, null=True)
    is_test = models.IntegerField()
    client = models.ForeignKey(DataentryClient, models.DO_NOTHING, blank=True, null=True)
    contactrequest = models.ForeignKey('self', models.DO_NOTHING, db_column='contactRequest_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DataEntry_contactrequest'


class DataentryContactrequesttypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    enum = models.IntegerField(db_column='eNum', blank=True, null=True)  # Field name made lowercase.
    is_test = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'DataEntry_contactrequesttypes'


class DataentryContract(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    created_at_date = models.DateField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_at_date = models.DateField(blank=True, null=True)
    serialnum = models.IntegerField(db_column='serialNum', unique=True, blank=True, null=True)  # Field name made lowercase.
    created_prev_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    is_test = models.IntegerField()
    belong_to = models.ForeignKey('DataentryEmployee', models.DO_NOTHING, blank=True, null=True)
    client = models.OneToOneField(DataentryClient, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('DataentryEmployee', models.DO_NOTHING, blank=True, null=True)
    modified_by = models.ForeignKey('DataentryEmployee', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DataEntry_contract'


class DataentryContractServices(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract = models.ForeignKey(DataentryContract, models.DO_NOTHING)
    service = models.ForeignKey('DataentryService', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'DataEntry_contract_services'
        unique_together = (('contract', 'service'),)


class DataentryDepartement(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    created_at_date = models.DateField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_at_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)
    is_test = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'DataEntry_departement'


class DataentryEmployee(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    created_at_date = models.DateField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_at_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)
    job2 = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    jobtitle = models.CharField(db_column='jobTitle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dateofemployment = models.DateField(db_column='dateOfEmployment', blank=True, null=True)  # Field name made lowercase.
    created_prev_date = models.DateField(blank=True, null=True)
    dateofbirth = models.DateField(db_column='dateOfBirth', blank=True, null=True)  # Field name made lowercase.
    naid = models.CharField(db_column='naId', max_length=14, blank=True, null=True)  # Field name made lowercase.
    typee = models.CharField(max_length=50, blank=True, null=True)
    salarytype = models.CharField(db_column='salaryType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    salary = models.IntegerField(blank=True, null=True)
    enum = models.IntegerField(db_column='eNum', unique=True, blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(blank=True, null=True)
    is_test = models.IntegerField()
    last_login = models.DateTimeField(blank=True, null=True)
    departement = models.ForeignKey(DataentryDepartement, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DataEntry_employee'


class DataentryFollowcontractservices(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    created_at_date = models.DateField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_at_date = models.DateField(blank=True, null=True)
    area = models.CharField(max_length=50, blank=True, null=True)
    startingdate = models.DateField(db_column='startingDate', blank=True, null=True)  # Field name made lowercase.
    serviceduedate = models.DateField(db_column='serviceDueDate', blank=True, null=True)  # Field name made lowercase.
    servicecollectdaystart = models.IntegerField(db_column='serviceCollectDayStart', blank=True, null=True)  # Field name made lowercase.
    servicecollectdayend = models.IntegerField(db_column='serviceCollectDayEnd', blank=True, null=True)  # Field name made lowercase.
    serviceduestatus = models.CharField(db_column='serviceDueStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    collcetstatusnums = models.CharField(db_column='collcetStatusNums', max_length=50, blank=True, null=True)  # Field name made lowercase.
    total_amount = models.IntegerField(blank=True, null=True)
    collected_amount = models.IntegerField(blank=True, null=True)
    collected_month = models.IntegerField(blank=True, null=True)
    collected_date = models.DateField(blank=True, null=True)
    remain_amount = models.IntegerField(blank=True, null=True)
    created_prev_date = models.DateField(blank=True, null=True)
    notes = models.CharField(max_length=100, blank=True, null=True)
    is_test = models.IntegerField()
    client = models.ForeignKey(DataentryClient, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(DataentryEmployee, models.DO_NOTHING, blank=True, null=True)
    modified_by = models.ForeignKey(DataentryEmployee, models.DO_NOTHING, blank=True, null=True)
    service = models.ForeignKey('DataentryService', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DataEntry_followcontractservices'


class DataentryOffers(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    created_at_date = models.DateField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_at_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.CharField(max_length=100)
    is_test = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'DataEntry_offers'


class DataentryRequestsimpleservice(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    created_at_date = models.DateField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_at_date = models.DateField(blank=True, null=True)
    is_test = models.IntegerField()
    client = models.ForeignKey(DataentryClient, models.DO_NOTHING, blank=True, null=True)
    service = models.ForeignKey('DataentrySimpleservice', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DataEntry_requestsimpleservice'


class DataentryService(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    created_at_date = models.DateField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_at_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    typee = models.CharField(max_length=50, blank=True, null=True)
    is_main = models.IntegerField()
    price = models.IntegerField()
    notes = models.TextField(blank=True, null=True)
    pricetype = models.TextField(db_column='priceType', blank=True, null=True)  # Field name made lowercase.
    billserial = models.IntegerField(db_column='billSerial', unique=True, blank=True, null=True)  # Field name made lowercase.
    billed_at = models.DateField(blank=True, null=True)
    fixeddeliverydate = models.IntegerField(db_column='fixedDeliveryDate', blank=True, null=True)  # Field name made lowercase.
    fixedpricecollectdate = models.IntegerField(db_column='fixedPriceCollectDate', blank=True, null=True)  # Field name made lowercase.
    fixedpricecollectdate_more = models.DateField(db_column='fixedPriceCollectDate_more', blank=True, null=True)  # Field name made lowercase.
    is_test = models.IntegerField()
    supervisor = models.ForeignKey(DataentryEmployee, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DataEntry_service'


class DataentrySimpleservice(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    created_at_date = models.DateField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_at_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    enum = models.IntegerField(db_column='eNum', blank=True, null=True)  # Field name made lowercase.
    is_test = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'DataEntry_simpleservice'


class DataentrySubservice(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_deleted = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    created_at_date = models.DateField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_at_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    baseservice = models.ForeignKey(DataentryService, models.DO_NOTHING, db_column='baseService_id', blank=True, null=True)  # Field name made lowercase.
    typee = models.ForeignKey('DataentryTypee', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DataEntry_subservice'


class DataentryTypee(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DataEntry_typee'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
