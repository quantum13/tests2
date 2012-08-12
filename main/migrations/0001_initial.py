# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Test'
        db.create_table('main_test', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=750)),
        ))
        db.send_create_signal('main', ['Test'])

        # Adding model 'Question'
        db.create_table('main_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('test', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Test'])),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=350)),
        ))
        db.send_create_signal('main', ['Question'])

        # Adding model 'Answer'
        db.create_table('main_answer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Test'])),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=350)),
            ('balls', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('main', ['Answer'])

        # Adding model 'Result'
        db.create_table('main_result', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('test', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Test'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('min_balls', self.gf('django.db.models.fields.IntegerField')()),
            ('max_balls', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('main', ['Result'])


    def backwards(self, orm):
        # Deleting model 'Test'
        db.delete_table('main_test')

        # Deleting model 'Question'
        db.delete_table('main_question')

        # Deleting model 'Answer'
        db.delete_table('main_answer')

        # Deleting model 'Result'
        db.delete_table('main_result')


    models = {
        'main.answer': {
            'Meta': {'object_name': 'Answer'},
            'balls': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Test']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '350'})
        },
        'main.question': {
            'Meta': {'object_name': 'Question'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'test': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Test']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '350'})
        },
        'main.result': {
            'Meta': {'object_name': 'Result'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_balls': ('django.db.models.fields.IntegerField', [], {}),
            'min_balls': ('django.db.models.fields.IntegerField', [], {}),
            'test': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Test']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'main.test': {
            'Meta': {'object_name': 'Test'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '750'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['main']