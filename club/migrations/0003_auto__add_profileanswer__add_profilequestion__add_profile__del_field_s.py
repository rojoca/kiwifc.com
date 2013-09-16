# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProfileAnswer'
        db.create_table(u'club_profileanswer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['club.ProfileQuestion'])),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answers', to=orm['club.Profile'])),
        ))
        db.send_create_signal(u'club', ['ProfileAnswer'])

        # Adding model 'ProfileQuestion'
        db.create_table(u'club_profilequestion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['club.Season'])),
        ))
        db.send_create_signal(u'club', ['ProfileQuestion'])

        # Adding model 'Profile'
        db.create_table(u'club_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('squad_member', self.gf('django.db.models.fields.related.ForeignKey')(related_name='profile', to=orm['club.SquadMember'])),
            ('profile', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('pic', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'club', ['Profile'])

        # Deleting field 'SquadMember.profile'
        db.delete_column(u'club_squadmember', 'profile')

        # Deleting field 'SquadMember.pic'
        db.delete_column(u'club_squadmember', 'pic')


    def backwards(self, orm):
        # Deleting model 'ProfileAnswer'
        db.delete_table(u'club_profileanswer')

        # Deleting model 'ProfileQuestion'
        db.delete_table(u'club_profilequestion')

        # Deleting model 'Profile'
        db.delete_table(u'club_profile')

        # Adding field 'SquadMember.profile'
        db.add_column(u'club_squadmember', 'profile',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'SquadMember.pic'
        db.add_column(u'club_squadmember', 'pic',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


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
            'last_season': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'l+'", 'null': 'True', 'to': u"orm['club.Season']"}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'club.profile': {
            'Meta': {'object_name': 'Profile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'profile': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'squad_member': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'profile'", 'to': u"orm['club.SquadMember']"})
        },
        u'club.profileanswer': {
            'Meta': {'object_name': 'ProfileAnswer'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers'", 'to': u"orm['club.Profile']"}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['club.ProfileQuestion']"})
        },
        u'club.profilequestion': {
            'Meta': {'object_name': 'ProfileQuestion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['club.Season']"})
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
            'pence_owing': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['club.Player']"}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'squad'", 'to': u"orm['club.Season']"})
        }
    }

    complete_apps = ['club']