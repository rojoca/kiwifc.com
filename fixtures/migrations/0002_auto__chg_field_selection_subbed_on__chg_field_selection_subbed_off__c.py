# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Selection.subbed_on'
        db.alter_column(u'fixtures_selection', 'subbed_on', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'Selection.subbed_off'
        db.alter_column(u'fixtures_selection', 'subbed_off', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'Selection.starting'
        db.alter_column(u'fixtures_selection', 'starting', self.gf('django.db.models.fields.BooleanField')())

    def backwards(self, orm):

        # Changing field 'Selection.subbed_on'
        db.alter_column(u'fixtures_selection', 'subbed_on', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Changing field 'Selection.subbed_off'
        db.alter_column(u'fixtures_selection', 'subbed_off', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Changing field 'Selection.starting'
        db.alter_column(u'fixtures_selection', 'starting', self.gf('django.db.models.fields.NullBooleanField')(null=True))

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
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['club.Season']"})
        },
        u'fixtures.card': {
            'Meta': {'object_name': 'Card'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reason': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fixtures.Selection']"})
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
            'opponent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fixtures.Opponent']"}),
            'played': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'postponed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fixtures.Venue']", 'null': 'True'})
        },
        u'fixtures.goal': {
            'Meta': {'object_name': 'Goal'},
            'assist': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'assists'", 'null': 'True', 'to': u"orm['fixtures.Selection']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'scorer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'goals'", 'to': u"orm['fixtures.Selection']"})
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
            'Meta': {'object_name': 'Selection'},
            'fixture': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'lineup'", 'to': u"orm['fixtures.Fixture']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'squad_member': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['club.SquadMember']"}),
            'starting': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subbed_off': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subbed_on': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'fixtures.venue': {
            'Meta': {'object_name': 'Venue'},
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['fixtures']