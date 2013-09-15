# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Player'
        db.create_table(u'club_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=32, null=True)),
            ('joined', self.gf('django.db.models.fields.related.ForeignKey')(related_name='new_players', to=orm['club.Season'])),
            ('last_season', self.gf('django.db.models.fields.related.ForeignKey')(related_name='l+', null=True, to=orm['club.Season'])),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'club', ['Player'])

        # Adding model 'SquadMember'
        db.create_table(u'club_squadmember', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['club.Season'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['club.Player'])),
            ('pence_owing', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'club', ['SquadMember'])

        # Adding model 'Season'
        db.create_table(u'club_season', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'club', ['Season'])

        # Adding model 'Date'
        db.create_table(u'club_date', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal(u'club', ['Date'])


    def backwards(self, orm):
        # Deleting model 'Player'
        db.delete_table(u'club_player')

        # Deleting model 'SquadMember'
        db.delete_table(u'club_squadmember')

        # Deleting model 'Season'
        db.delete_table(u'club_season')

        # Deleting model 'Date'
        db.delete_table(u'club_date')


    models = {
        u'club.date': {
            'Meta': {'object_name': 'Date'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'club.player': {
            'Meta': {'object_name': 'Player'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joined': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'new_players'", 'to': u"orm['club.Season']"}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'last_season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'l+'", 'null': 'True', 'to': u"orm['club.Season']"}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'club.season': {
            'Meta': {'object_name': 'Season'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'club.squadmember': {
            'Meta': {'object_name': 'SquadMember'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pence_owing': ('django.db.models.fields.IntegerField', [], {}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['club.Player']"}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['club.Season']"})
        }
    }

    complete_apps = ['club']