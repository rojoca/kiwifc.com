# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MatchReport.title'
        db.add_column(u'manager_matchreport', 'title',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MatchReport.title'
        db.delete_column(u'manager_matchreport', 'title')


    models = {
        u'club.player': {
            'Meta': {'object_name': 'Player'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joined': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'new_players'", 'to': u"orm['club.Season']"}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'last_season': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'l+'", 'null': 'True', 'to': u"orm['club.Season']"}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
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
            'season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'squad'", 'to': u"orm['club.Season']"})
        },
        u'fixtures.fixture': {
            'Meta': {'object_name': 'Fixture'},
            'cancelled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'defaulted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'goals_conceded': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'goals_scored': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'home_game': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fixtures.League']"}),
            'lineup': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['club.SquadMember']", 'through': u"orm['fixtures.Selection']", 'symmetrical': 'False'}),
            'opponent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fixtures.Opponent']"}),
            'played': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'postponed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fixtures.Venue']", 'null': 'True'})
        },
        u'fixtures.league': {
            'Meta': {'object_name': 'League'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['club.Season']"})
        },
        u'fixtures.opponent': {
            'Meta': {'object_name': 'Opponent'},
            'home_ground': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fixtures.Venue']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'fixtures.selection': {
            'Meta': {'unique_together': "(('fixture', 'squad_member'),)", 'object_name': 'Selection'},
            'fixture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fixtures.Fixture']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'squad_member': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'selected_for'", 'to': u"orm['club.SquadMember']"}),
            'starting': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'fixtures.venue': {
            'Meta': {'object_name': 'Venue'},
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'manager.fine': {
            'Meta': {'object_name': 'Fine'},
            'amount': ('django.db.models.fields.IntegerField', [], {'default': '50'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fixture': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fines'", 'null': 'True', 'to': u"orm['fixtures.Fixture']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reason': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['club.SquadMember']"})
        },
        u'manager.matchreport': {
            'Meta': {'object_name': 'MatchReport'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['club.SquadMember']"}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fixture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fixtures.Fixture']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'report': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'manager.prematch': {
            'Meta': {'object_name': 'Prematch'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['club.SquadMember']"}),
            'beer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fixture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fixtures.Fixture']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'theme': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['manager']