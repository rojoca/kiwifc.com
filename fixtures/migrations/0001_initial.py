# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'League'
        db.create_table(u'fixtures_league', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['club.Season'])),
        ))
        db.send_create_signal(u'fixtures', ['League'])

        # Adding model 'Venue'
        db.create_table(u'fixtures_venue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'fixtures', ['Venue'])

        # Adding model 'Opponent'
        db.create_table(u'fixtures_opponent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('home_ground', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fixtures.Venue'], null=True)),
        ))
        db.send_create_signal(u'fixtures', ['Opponent'])

        # Adding model 'Fixture'
        db.create_table(u'fixtures_fixture', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('opponent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fixtures.Opponent'])),
            ('venue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fixtures.Venue'], null=True)),
            ('league', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fixtures.League'])),
            ('home_game', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('defaulted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('postponed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cancelled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('played', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('goals_scored', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('goals_conceded', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'fixtures', ['Fixture'])

        # Adding model 'Selection'
        db.create_table(u'fixtures_selection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fixture', self.gf('django.db.models.fields.related.ForeignKey')(related_name='lineup', to=orm['fixtures.Fixture'])),
            ('squad_member', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['club.SquadMember'])),
            ('starting', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('subbed_on', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('subbed_off', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'fixtures', ['Selection'])

        # Adding model 'Goal'
        db.create_table(u'fixtures_goal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scorer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='goals', to=orm['fixtures.Selection'])),
            ('assist', self.gf('django.db.models.fields.related.ForeignKey')(related_name='assists', null=True, to=orm['fixtures.Selection'])),
            ('minute', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal(u'fixtures', ['Goal'])

        # Adding model 'Card'
        db.create_table(u'fixtures_card', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('recipient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fixtures.Selection'])),
            ('minute', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('reason', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal(u'fixtures', ['Card'])


    def backwards(self, orm):
        # Deleting model 'League'
        db.delete_table(u'fixtures_league')

        # Deleting model 'Venue'
        db.delete_table(u'fixtures_venue')

        # Deleting model 'Opponent'
        db.delete_table(u'fixtures_opponent')

        # Deleting model 'Fixture'
        db.delete_table(u'fixtures_fixture')

        # Deleting model 'Selection'
        db.delete_table(u'fixtures_selection')

        # Deleting model 'Goal'
        db.delete_table(u'fixtures_goal')

        # Deleting model 'Card'
        db.delete_table(u'fixtures_card')


    models = {
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
        },
        u'fixtures.card': {
            'Meta': {'object_name': 'Card'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'reason': ('django.db.models.fields.TextField', [], {'null': 'True'}),
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
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
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
            'starting': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'subbed_off': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'subbed_on': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        u'fixtures.venue': {
            'Meta': {'object_name': 'Venue'},
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['fixtures']