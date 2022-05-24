from ekklesia_shared.models import Organization, Domain
tenant = Organization(schema_name="public", name='Public Schema')
tenant.save()

domain = Domain()
domain.domain = 'localhost' # don't add your port or www here! on a local server you'll want to use localhost here
domain.tenant = tenant
domain.is_primary = True
domain.save()


# create your first real tenant
tenant = Organization(schema_name='goodsheeperd',
                name='Iglesia de Dios El Buen Pastor')
tenant.save() # migrate_schemas automatically called, your tenant is ready to be used!

# Add one or more domains for the tenant
domain = Domain()
domain.domain = 'goodsheeperd.localhost' # don't add your port or www here!
domain.tenant = tenant
domain.is_primary = True
domain.save()