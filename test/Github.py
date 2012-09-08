# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import Framework

class Github( Framework.TestCase ):
    def testGetGists( self ):
        self.assertListKeyBegin( self.g.get_gists(), lambda g: g.id, [ "2729695", "2729656", "2729597", "2729584", "2729569", "2729554", "2729543", "2729537", "2729536", "2729533", "2729525", "2729522", "2729519", "2729515", "2729506", "2729487", "2729484", "2729482", "2729441", "2729432", "2729420", "2729398", "2729372", "2729371", "2729351", "2729346", "2729316", "2729304", "2729296", "2729276", "2729272", "2729265", "2729195", "2729160", "2729143", "2729127", "2729119", "2729113", "2729103", "2729069", "2729059", "2729051", "2729029", "2729027", "2729026", "2729022", "2729002", "2728985", "2728979", "2728964", "2728937", "2728933", "2728884", "2728869", "2728866", "2728855", "2728854", "2728853", "2728846", "2728825", "2728814", "2728813", "2728812", "2728805", "2728802", "2728800", "2728798", "2728797", "2728796", "2728793", "2728758", "2728754", "2728751", "2728748", "2728721", "2728716", "2728715", "2728705", "2728701", "2728699", "2728697", "2728688", "2728683", "2728677", "2728649", "2728640", "2728625", "2728620", "2728615", "2728614", "2728565", "2728564", "2728554", "2728523", "2728519", "2728511", "2728497", "2728496", "2728495", "2728487" ] )

    def testLegacySearchRepos( self ):
        repos = self.g.legacy_search_repos( "github api v3" )
        self.assertListKeyBegin( repos, lambda r: r.name, [ "octokit", "github-v3-api", "github_v3_api" ] )
        self.assertEqual( repos[ 0 ].full_name, "pengwynn/octokit" )

    def testLegacySearchReposPagination( self ):
        repos = self.g.legacy_search_repos( "document" )
        self.assertListKeyBegin( repos, lambda r: r.name, [ "git", "nimbus", "kss", "sstoolkit", "lawnchair", "appledoc", "jQ.Mobi", "ipython", "mongoengine", "ravendb", "substance", "symfony-docs", "JavaScript-Garden", "DocSets-for-iOS", "yard", "phpDocumentor2", "phpsh", "Tangle", "Ingredients", "documentjs", "xhp", "couchdb-lucene", "dox", "magento2", "javascriptmvc", "FastPdfKit", "roar", "DocumentUp", "NoRM", "jsdoc", "tagger", "mongodb-csharp", "php-github-api", "beautiful-docs", "mongodb-odm", "iodocs", "seesaw", "bcx-api", "developer.github.com", "amqp", "docsplit", "pycco", "standards-and-practices", "tidy-html5", "redis-doc", "tomdoc", "docs", "flourish", "userguide", "swagger-ui", "rfc", "Weasel-Diesel", "yuidoc", "apigen", "document-viewer", "develop.github.com", "Shanty-Mongo", "PTShowcaseViewController", "gravatar_image_tag", "api-wow-docs", "mongoid-tree", "safari-json-formatter", "mayan", "orm-documentation", "jsfiddle-docs-alpha", "core", "documentcloud", "flexible-nav", "writeCapture", "readium", "xmldocument", "Documentation-Examples", "grails-doc", "stdeb", "aws-autoscaling", "voteable_mongo", "review", "spreadsheet_on_rails", "UKSyntaxColoredTextDocument", "mandango", "bdoc", "Documentation", "documents.com", "rghost", "ticket_mule", "vendo", "khan-api", "spring-data-document-examples", "rspec_api_documentation", "axlsx", "phpdox", "documentation", "Sami", "innershiv", "doxyclean", "documents", "rvm-site", "jqapi", "documentation", "hadoopy", "VichUploaderBundle", "pdoc", "documentation", "wii-js", "oss-docs", "scala-maven-plugin", "Documents", "documenter", "behemoth", "documentation", "documentation", "propelorm.github.com", "Kobold2D", "AutoObjectDocumentation", "php-mongodb-admin", "django-mongokit", "puppet-docs", "docs", "Document", "vendorer", "symfony1-docs", "shocco", "documentation", "jog", "docs", "documentation", "documentation", "documentation", "documentation", "Documentation", "documentation", "documentation", "phpunit-documentation", "ADCtheme", "NelmioApiDocBundle", "iCloud-Singleton-CloudMe", "Documentation", "document", "document_mapper", "heroku-docs", "couchdb-odm", "documentation", "documentation", "document", "documentation", "NanoStore", "documentation", "Documentation", "documentation", "Documentation", "documentation", "document", "documentation", "documentation", "Documentation", "Documentation", "grendel", "ceylon-compiler", "mbtiles-spec", "documentation", "documents", "documents", "Documents", "Documentation", "documentation", "Documentation", "documentation", "documents", "Documentation", "documentation", "documentation", "documents", "Documentation", "documentation", "documenter", "documentation", "documents", "Documents", "documents", "documents", "documentation", "Document", "document", "rdoc", "mongoid_token", "travis-ci.github.com", "Documents", "Documents", "documents", "Document", "Documentation", "documents", "Documents", "Documentation", "documents", "documents", "documents", "documentation", "Documents", "Document", "documents", "documents", "Documentation", "Documentation", "Document", "documents", "Documents", "Documents", "Documentation", "Documents", "documents", "Documents", "document", "documents", "Documentation", "Documents", "documents", "documents", "Documents", "documents", "Documentation", "documentation", "Document", "Documents", "documents", "documents", "documents", "Documentation", "Documentation", "Documents", "Documents", "Documents", "Documenter", "document", "Documentation", "Documents", "Documents", "documentation", "documentation", "Document", "Documents", "Documentation", "Documentation", "Documents", "documents", "Documents", "document", "documentation", "Documents", "documentation", "documentation", "documentation", "Documentation", "Documents", "Documents", "documentation", "Documents", "Documents", "documentation", "documentation", "documents", "Documentation", "documents", "documentation", "Documentation", "Documents", "documentation", "documentation", "documents", "documentation", "Umbraco5Docs", "documents", "Documents", "Documentation", "documents", "document", "documents", "document", "documents", "documentation", "Documents", "documents", "document", "Documents", "Documentation", "Documentation", "documentation", "Documentation", "document", "documentation", "documents", "documents", "Documentations", "document", "documentation", "Documentation", "Document", "Documents", "Documents", "Document" ] )

    def testLegacySearchReposWithLanguage( self ):
        repos = self.g.legacy_search_repos( "document", language = "Python" )
        self.assertListKeyBegin( repos, lambda r: r.name, [ "ipython", "mongoengine", "tagger" ] )
        self.assertEqual( repos[ 0 ].full_name, "ipython/ipython" )

    def testLegacySearchUsers( self ):
        self.assertListKeyBegin( self.g.legacy_search_users( "vincent" ), lambda u: u.login, [ "nvie", "obra", "lusis" ] )

    def testLegacySearchUsersPagination( self ):
        self.assertEqual( len( list( self.g.legacy_search_users( "Lucy" ) ) ), 146 )

    def testLegacySearchUserByEmail( self ):
        user = self.g.legacy_search_user_by_email( "vincent@vincent-jacques.net" )
        self.assertEqual( user.login, "jacquev6" )
        self.assertEqual( user.followers, 13 )

    def testGetHooks( self ):
        hooks = self.g.get_hooks()
        hook = hooks[ 0 ]
        self.assertEqual( hook.name, "activecollab" )
        self.assertEqual( hook.supported_events, [ "push" ] )
        self.assertEqual( hook.events, [ "push" ] )
        self.assertEqual( hook.schema, [ [ "string", "url" ], [ "string", "token" ], [ "string", "project_id" ], [ "string", "milestone_id" ], [ "string", "category_id" ] ] )
