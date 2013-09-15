# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FixtureDate'
        db.create_table(u'availability_fixturedate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['club.Season'])),
            ('fixture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fixtures.Fixture'], null=True)),
        ))
        db.send_create_signal(u'availability', ['FixtureDate'])

        # Adding model 'YesNoAnswer'
        db.create_table(u'availability_yesnoanswer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['availability.FixtureDate'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['club.SquadMember'])),
            ('yes', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'availability', ['YesNoAnswer'])

        # Adding model 'OptionAnswer'
        db.create_table(u'availability_optionanswer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['availability.FixtureDate'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['club.SquadMember'])),
            ('option', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'availability', ['OptionAnswer'])


    def backwards(self, orm):
        # Deleting model 'FixtureDate'
        db.delete_table(u'availability_fixturedate')

        # Deleting model 'YesNoAnswer'
        db.delete_table(u'availability_yesnoanswer')

        # Deleting model 'OptionAnswer'
        db.delete_table(u'availability_optionanswer')


    models = {
        u'availability.fixturedate': {
            'Meta': {'object_name': 'FixtureDate'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'fixture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fixtures.Fixture']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['club.Season']"})
        },
        u'availability.optionanswer': {
            'Meta': {'object_name': 'OptionAnswer'},
            'date': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['availability.FixtureDate']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'option': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['club.SquadMember']"})
        },
        u'availability.yesnoanswer': {
            'Meta': {'object_name': 'YesNoAnswer'},
            'date': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['availability.FixtureDate']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['club.SquadMember']"}),
            'yes': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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
        u'fixtures.venue': {
            'Meta': {'object_name': 'Venue'},
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['availability']