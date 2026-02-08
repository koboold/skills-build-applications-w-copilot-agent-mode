from django.db import migrations

def create_email_unique_index(apps, schema_editor):
    from djongo.database import connect
    client = connect()
    db = client['octofit_db']
    db['octofit_tracker_user'].create_index('email', unique=True)

def drop_email_unique_index(apps, schema_editor):
    from djongo.database import connect
    client = connect()
    db = client['octofit_db']
    db['octofit_tracker_user'].drop_index('email_1')

class Migration(migrations.Migration):
    dependencies = [
        ('octofit_tracker', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(create_email_unique_index, drop_email_unique_index),
    ]
