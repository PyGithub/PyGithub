# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jakub Wilk <jwilk@jwilk.net>                                  #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Maarten Fonville <mfonville@users.noreply.github.com>         #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################


REQ_IF_NONE_MATCH = "If-None-Match"
REQ_IF_MODIFIED_SINCE = "If-Modified-Since"
PROCESSING_202_WAIT_TIME = 2

# ##############################################################################
# Response Header                                                              #
# (Lower Case)                                                                 #
# ##############################################################################
RES_ETAG = "etag"
RES_LAST_MODIFIED = "last-modified"

# Inspired by https://github.com/google/go-github

# Headers

headerRateLimit = "x-ratelimit-limit"
headerRateRemaining = "x-ratelimit-remaining"
headerRateReset = "x-ratelimit-reset"
headerOTP = "X-GitHub-OTP"

defaultMediaType = "application/octet-stream"

# Custom media type for preview API

# https://developer.github.com/changes/2014-12-09-new-attributes-for-stars-api/
mediaTypeStarringPreview = "application/vnd.github.v3.star+json"

# https://developer.github.com/changes/2016-02-19-source-import-preview-api/
mediaTypeImportPreview = "application/vnd.github.barred-rock-preview"

# https://developer.github.com/changes/2016-05-12-reactions-api-preview/
mediaTypeReactionsPreview = "application/vnd.github.squirrel-girl-preview"

# https://developer.github.com/changes/2016-09-14-Integrations-Early-Access/
mediaTypeIntegrationPreview = "application/vnd.github.machine-man-preview+json"

# https://developer.github.com/changes/2016-09-14-projects-api/
mediaTypeProjectsPreview = "application/vnd.github.inertia-preview+json"

# https://developer.github.com/changes/2017-01-05-commit-search-api/
mediaTypeCommitSearchPreview = "application/vnd.github.cloak-preview"

# https://developer.github.com/changes/2017-02-28-user-blocking-apis-and-webhook/
mediaTypeBlockUsersPreview = "application/vnd.github.giant-sentry-fist-preview+json"

# https://developer.github.com/changes/2017-07-17-update-topics-on-repositories/
mediaTypeTopicsPreview = "application/vnd.github.mercy-preview+json"

# https://developer.github.com/changes/2018-02-22-label-description-search-preview/
mediaTypeLabelDescriptionSearchPreview = "application/vnd.github.symmetra-preview+json"

# https://developer.github.com/changes/2018-01-10-lock-reason-api-preview/
mediaTypeLockReasonPreview = "application/vnd.github.sailor-v-preview+json"

# https://developer.github.com/changes/2018-01-25-organization-invitation-api-preview/
mediaTypeOrganizationInvitationPreview = "application/vnd.github.dazzler-preview+json"

# https://developer.github.com/changes/2018-03-16-protected-branches-required-approving-reviews/
mediaTypeRequireMultipleApprovingReviews = "application/vnd.github.luke-cage-preview+json"

# https://developer.github.com/v3/search/#highlighting-code-search-results-1
highLightSearchPreview = "application/vnd.github.v3.text-match+json"
