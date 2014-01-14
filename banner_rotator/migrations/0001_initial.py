# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Campaign'
        db.create_table(u'banner_rotator_campaign', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'banner_rotator', ['Campaign'])

        # Adding model 'Place'
        db.create_table(u'banner_rotator_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('width', self.gf('django.db.models.fields.SmallIntegerField')(default=None, null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.SmallIntegerField')(default=None, null=True, blank=True)),
        ))
        db.send_create_signal(u'banner_rotator', ['Place'])

        # Adding unique constraint on 'Place', fields ['slug']
        db.create_unique(u'banner_rotator_place', ['slug'])

        # Adding model 'Banner'
        db.create_table(u'banner_rotator_banner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('campaign', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='banners', null=True, blank=True, to=orm['banner_rotator.Campaign'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('alt', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('url_target', self.gf('django.db.models.fields.CharField')(default='', max_length=10)),
            ('views', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('max_views', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('max_clicks', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('start_at', self.gf('django.db.models.fields.DateTimeField')(default=None, null=True, blank=True)),
            ('finish_at', self.gf('django.db.models.fields.DateTimeField')(default=None, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('click_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, null=True)),
        ))
        db.send_create_signal(u'banner_rotator', ['Banner'])

        # Adding M2M table for field places on 'Banner'
        m2m_table_name = db.shorten_name(u'banner_rotator_banner_places')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('banner', models.ForeignKey(orm[u'banner_rotator.banner'], null=False)),
            ('place', models.ForeignKey(orm[u'banner_rotator.place'], null=False))
        ))
        db.create_unique(m2m_table_name, ['banner_id', 'place_id'])

        # Adding model 'Click'
        db.create_table(u'banner_rotator_click', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('banner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='clicks', to=orm['banner_rotator.Banner'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='banner_clicks', null=True, to=orm['auth.User'])),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True, blank=True)),
            ('user_agent', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('referrer', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'banner_rotator', ['Click'])


    def backwards(self, orm):
        # Removing unique constraint on 'Place', fields ['slug']
        db.delete_unique(u'banner_rotator_place', ['slug'])

        # Deleting model 'Campaign'
        db.delete_table(u'banner_rotator_campaign')

        # Deleting model 'Place'
        db.delete_table(u'banner_rotator_place')

        # Deleting model 'Banner'
        db.delete_table(u'banner_rotator_banner')

        # Removing M2M table for field places on 'Banner'
        db.delete_table(db.shorten_name(u'banner_rotator_banner_places'))

        # Deleting model 'Click'
        db.delete_table(u'banner_rotator_click')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'banner_rotator.banner': {
            'Meta': {'object_name': 'Banner'},
            'alt': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'banners'", 'null': 'True', 'blank': 'True', 'to': u"orm['banner_rotator.Campaign']"}),
            'click_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'finish_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'max_clicks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'max_views': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'places': ('django.db.models.fields.related.ManyToManyField', [], {'db_index': 'True', 'related_name': "'banners'", 'symmetrical': 'False', 'to': u"orm['banner_rotator.Place']"}),
            'start_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'url_target': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '5'})
        },
        u'banner_rotator.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'banner_rotator.click': {
            'Meta': {'object_name': 'Click'},
            'banner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'clicks'", 'to': u"orm['banner_rotator.Banner']"}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'referrer': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'banner_clicks'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_agent': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'banner_rotator.place': {
            'Meta': {'unique_together': "(('slug',),)", 'object_name': 'Place'},
            'height': ('django.db.models.fields.SmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'width': ('django.db.models.fields.SmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['banner_rotator']