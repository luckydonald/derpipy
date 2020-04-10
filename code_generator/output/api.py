from models import *

routes = [
	Route(name='comment', method='GET', path=UrlPath(original='/api/v1/json/comments/:comment_id', template='/api/v1/json/comments/{comment_id}', params=[Parameter(name='comment_id', type='Integer', description='the variable comment_id part of the url.', optional=False)]), allowed_query_parameters=[], description='Fetches a **comment response** for the comment ID referenced by the `comment_id` URL parameter.', response_format=ResponseType(schema='{"comment":Comment}', is_list=False, key='comment', class_name='Comment'), example_url='/api/v1/json/comments/1000'),
	Route(name='image', method='GET', path=UrlPath(original='/api/v1/json/images/:image_id', template='/api/v1/json/images/{image_id}', params=[Parameter(name='image_id', type='Integer', description='the variable image_id part of the url.', optional=False)]), allowed_query_parameters=[Parameter(name='key', type='String', description='An optional authentication token. If omitted, no user will be authenticated.\n\nYou can find your authentication token in your [account settings](https://derpibooru.org/registration/edit).', optional=True), Parameter(name='filter_id', type='Integer', description='Assuming the user can access the filter ID given by the parameter, overrides the current filter for this request. This is primarily useful for unauthenticated API access.', optional=False)], description='Fetches an **image response** for the image ID referenced by the `image_id` URL parameter.', response_format=ResponseType(schema='{"image":Image}', is_list=False, key='image', class_name='Image'), example_url='/api/v1/json/images/1'),
	Route(name='featured_images', method='GET', path=UrlPath(original='/api/v1/json/images/featured', template='/api/v1/json/images/featured', params=[]), allowed_query_parameters=[], description='Fetches an **image response** for the for the current featured image.', response_format=ResponseType(schema='{"image":Image}', is_list=False, key='image', class_name='Image'), example_url='/api/v1/json/images/featured'),
	Route(name='tag', method='GET', path=UrlPath(original='/api/v1/json/tags/:tag_id', template='/api/v1/json/tags/{tag_id}', params=[Parameter(name='tag_id', type='Integer', description='the variable tag_id part of the url.', optional=False)]), allowed_query_parameters=[], description="Fetches a **tag response** for the **tag slug** given by the `tag_id` URL parameter. The tag's ID is **not** used.", response_format=ResponseType(schema='{"tag":Tag}', is_list=False, key='tag', class_name='Tag'), example_url='/api/v1/json/tags/artist-colon-atryl'),
	Route(name='post', method='GET', path=UrlPath(original='/api/v1/json/posts/:post_id', template='/api/v1/json/posts/{post_id}', params=[Parameter(name='post_id', type='Integer', description='the variable post_id part of the url.', optional=False)]), allowed_query_parameters=[], description='Fetches a **post response** for the post ID given by the `post_id` URL parameter.', response_format=ResponseType(schema='{"post":Post}', is_list=False, key='post', class_name='Post'), example_url='/api/v1/json/posts/2730144'),
	Route(name='user', method='GET', path=UrlPath(original='/api/v1/json/profiles/:user_id', template='/api/v1/json/profiles/{user_id}', params=[Parameter(name='user_id', type='Integer', description='the variable user_id part of the url.', optional=False)]), allowed_query_parameters=[], description='Fetches a **profile response** for the user ID given by the `user_id` URL parameter.', response_format=ResponseType(schema='{"user":User}', is_list=False, key='user', class_name='User'), example_url='/api/v1/json/profiles/216494'),
	Route(name='filter', method='GET', path=UrlPath(original='/api/v1/json/filters/:filter_id', template='/api/v1/json/filters/{filter_id}', params=[Parameter(name='filter_id', type='Integer', description='the variable filter_id part of the url.', optional=False)]), allowed_query_parameters=[Parameter(name='key', type='String', description='An optional authentication token. If omitted, no user will be authenticated.\n\nYou can find your authentication token in your [account settings](https://derpibooru.org/registration/edit).', optional=True)], description='Fetches a **filter response** for the filter ID given by the `filter_id` URL parameter.', response_format=ResponseType(schema='{"filter":Filter}', is_list=False, key='filter', class_name='Filter'), example_url='/api/v1/json/filters/56027'),
	Route(name='system_filters', method='GET', path=UrlPath(original='/api/v1/json/filters/system', template='/api/v1/json/filters/system', params=[]), allowed_query_parameters=[Parameter(name='page', type='Integer', description='Controls the current page of the response, if the response is paginated. Empty values default to the first page.', optional=False)], description='Fetches a list of **filter responses** that are flagged as being **system** filters (and thus usable by anyone).', response_format=ResponseType(schema='{"filters":[Filter]}', is_list=True, key='filters', class_name='Filter'), example_url='/api/v1/json/filters/system'),
	Route(name='user_filters', method='GET', path=UrlPath(original='/api/v1/json/filters/user', template='/api/v1/json/filters/user', params=[]), allowed_query_parameters=[Parameter(name='key', type='String', description='An optional authentication token. If omitted, no user will be authenticated.\n\nYou can find your authentication token in your [account settings](https://derpibooru.org/registration/edit).', optional=True), Parameter(name='page', type='Integer', description='Controls the current page of the response, if the response is paginated. Empty values default to the first page.', optional=False)], description='Fetches a list of **filter responses** that belong to the user given by **key**. If no **key** is given or it is invalid, will return a **403 Forbidden** error.', response_format=ResponseType(schema='{"filters":[Filter]}', is_list=True, key='filters', class_name='Filter'), example_url='/api/v1/json/filters/user'),
	Route(name='oembed', method='GET', path=UrlPath(original='/api/v1/json/oembed', template='/api/v1/json/oembed', params=[]), allowed_query_parameters=[Parameter(name='version', type='String', description='Link a deviantART page, a Tumblr post, or the image directly.', optional=False)], description='Fetches an **oEmbed response** for the given app link or CDN URL.', response_format=ResponseType(schema='Oembed', is_list=False, key=None, class_name='Oembed'), example_url='/api/v1/json/oembed?url=https://derpicdn.net/img/2012/1/2/3/full.png'),
	Route(name='search_comments', method='GET', path=UrlPath(original='/api/v1/json/search/comments', template='/api/v1/json/search/comments', params=[]), allowed_query_parameters=[Parameter(name='key', type='String', description='An optional authentication token. If omitted, no user will be authenticated.\n\nYou can find your authentication token in your [account settings](https://derpibooru.org/registration/edit).', optional=True), Parameter(name='page', type='Integer', description='Controls the current page of the response, if the response is paginated. Empty values default to the first page.', optional=False)], description='Executes the search given by the `q` query parameter, and returns **comment responses** sorted by descending creation time.', response_format=ResponseType(schema='{"comments":[Comment]}', is_list=True, key='comments', class_name='Comment'), example_url='/api/v1/json/search/comments?q=image_id:1000000'),
	Route(name='search_galleries', method='GET', path=UrlPath(original='/api/v1/json/search/galleries', template='/api/v1/json/search/galleries', params=[]), allowed_query_parameters=[Parameter(name='key', type='String', description='An optional authentication token. If omitted, no user will be authenticated.\n\nYou can find your authentication token in your [account settings](https://derpibooru.org/registration/edit).', optional=True), Parameter(name='page', type='Integer', description='Controls the current page of the response, if the response is paginated. Empty values default to the first page.', optional=False)], description='Executes the search given by the `q` query parameter, and returns **gallery responses** sorted by descending creation time.', response_format=ResponseType(schema='{"galleries":[Gallery]}', is_list=True, key='galleries', class_name='Gallery'), example_url='/api/v1/json/search/galleries?q=title:mean*'),
	Route(name='search_posts', method='GET', path=UrlPath(original='/api/v1/json/search/posts', template='/api/v1/json/search/posts', params=[]), allowed_query_parameters=[Parameter(name='key', type='String', description='An optional authentication token. If omitted, no user will be authenticated.\n\nYou can find your authentication token in your [account settings](https://derpibooru.org/registration/edit).', optional=True), Parameter(name='page', type='Integer', description='Controls the current page of the response, if the response is paginated. Empty values default to the first page.', optional=False)], description='Executes the search given by the `q` query parameter, and returns **post responses** sorted by descending creation time.', response_format=ResponseType(schema='{"posts":[Post]}', is_list=True, key='posts', class_name='Post'), example_url='/api/v1/json/search/posts?q=subject:time wasting thread'),
	Route(name='search_images', method='GET', path=UrlPath(original='/api/v1/json/search/images', template='/api/v1/json/search/images', params=[]), allowed_query_parameters=[Parameter(name='key', type='String', description='An optional authentication token. If omitted, no user will be authenticated.\n\nYou can find your authentication token in your [account settings](https://derpibooru.org/registration/edit).', optional=True), Parameter(name='filter_id', type='Integer', description='Assuming the user can access the filter ID given by the parameter, overrides the current filter for this request. This is primarily useful for unauthenticated API access.', optional=False), Parameter(name='page', type='Integer', description='Controls the current page of the response, if the response is paginated. Empty values default to the first page.', optional=False), Parameter(name='per_page', type='Integer', description='Controls the number of results per page, up to a limit of 50, if the response is paginated. The default is 25.', optional=False), Parameter(name='q', type='String', description='The current search query, if the request is a search request.', optional=False), Parameter(name='sd', type='String', description='The current sort direction, if the request is a search request.', optional=False), Parameter(name='sf', type='String', description='The current sort field, if the request is a search request.', optional=False)], description='Executes the search given by the `q` query parameter, and returns **image responses**.', response_format=ResponseType(schema='{"images":[Image]}', is_list=True, key='images', class_name='Image'), example_url='/api/v1/json/search/images?q=safe'),
	Route(name='search_tags', method='GET', path=UrlPath(original='/api/v1/json/search/tags', template='/api/v1/json/search/tags', params=[]), allowed_query_parameters=[Parameter(name='page', type='Integer', description='Controls the current page of the response, if the response is paginated. Empty values default to the first page.', optional=False)], description='Executes the search given by the `q` query parameter, and returns **tag responses** sorted by descending image count.', response_format=ResponseType(schema='{"tags":[Tag]}', is_list=True, key='tags', class_name='Tag'), example_url='/api/v1/json/search/tags?q=analyzed_name:wing'),
	Route(name='search_reverse', method='POST', path=UrlPath(original='/api/v1/json/search/reverse', template='/api/v1/json/search/reverse', params=[]), allowed_query_parameters=[Parameter(name='key', type='String', description='An optional authentication token. If omitted, no user will be authenticated.\n\nYou can find your authentication token in your [account settings](https://derpibooru.org/registration/edit).', optional=True), Parameter(name='version', type='String', description='Link a deviantART page, a Tumblr post, or the image directly.', optional=False), Parameter(name='version', type='Float', description='Match distance (suggested values: between 0.2 and 0.5).', optional=False)], description='Returns **image responses** based on the results of reverse-searching the image given by the `url` query parameter.', response_format=ResponseType(schema='{"images":[Image]}', is_list=True, key='images', class_name='Image'), example_url='/api/v1/json/search/reverse?url=https://derpicdn.net/img/2019/12/24/2228439/full.jpg'),
	Route(name='forums', method='GET', path=UrlPath(original='/api/v1/json/forums', template='/api/v1/json/forums', params=[]), allowed_query_parameters=[], description='Fetches a list of **forum responses**.', response_format=ResponseType(schema='{"forums":Forum}', is_list=False, key='forums', class_name='Forum'), example_url='/api/v1/json/forums'),
	Route(name='forum', method='GET', path=UrlPath(original='/api/v1/json/forums/:short_name', template='/api/v1/json/forums/{short_name}', params=[Parameter(name='short_name', type='String', description='the variable short_name part of the url.', optional=False)]), allowed_query_parameters=[], description='Fetches a **forum response** for the abbreviated name given by the `short_name` URL parameter.', response_format=ResponseType(schema='{"forum":Forum}', is_list=False, key='forum', class_name='Forum'), example_url='/api/v1/json/forums/dis'),
	Route(name='forum_topics', method='GET', path=UrlPath(original='/api/v1/json/forums/:short_name/topics', template='/api/v1/json/forums/{short_name}/topics', params=[Parameter(name='short_name', type='String', description='the variable short_name part of the url.', optional=False)]), allowed_query_parameters=[Parameter(name='page', type='Integer', description='Controls the current page of the response, if the response is paginated. Empty values default to the first page.', optional=False)], description='Fetches a list of **topic responses** for the abbreviated forum name given by the `short_name` URL parameter.', response_format=ResponseType(schema='{"topics":Topic}', is_list=False, key='topics', class_name='Topic'), example_url='/api/v1/json/forums/dis/topics'),
	Route(name='forum_topic', method='GET', path=UrlPath(original='/api/v1/json/forums/:short_name/topics/:topic_slug', template='/api/v1/json/forums/{short_name}/topics/{topic_slug}', params=[Parameter(name='short_name', type='String', description='the variable short_name part of the url.', optional=False), Parameter(name='topic_slug', type='String', description='the variable topic_slug part of the url.', optional=False)]), allowed_query_parameters=[], description='Fetches a **topic response** for the abbreviated forum name given by the `short_name` and topic given by `topic_slug` URL parameters.', response_format=ResponseType(schema='{"topic":Topic}', is_list=False, key='topic', class_name='Topic'), example_url='/api/v1/json/forums/dis/topics/ask-the-mods-anything'),
	Route(name='forum_posts', method='GET', path=UrlPath(original='/api/v1/json/forums/:short_name/topics/:topic_slug/posts', template='/api/v1/json/forums/{short_name}/topics/{topic_slug}/posts', params=[Parameter(name='short_name', type='String', description='the variable short_name part of the url.', optional=False), Parameter(name='topic_slug', type='String', description='the variable topic_slug part of the url.', optional=False)]), allowed_query_parameters=[Parameter(name='page', type='Integer', description='Controls the current page of the response, if the response is paginated. Empty values default to the first page.', optional=False)], description='Fetches a list of **post responses** for the abbreviated forum name given by the `short_name` and topic given by `topic_slug` URL parameters.', response_format=ResponseType(schema='{"posts":Post}', is_list=False, key='posts', class_name='Post'), example_url='/api/v1/json/forums/dis/topics/ask-the-mods-anything/posts'),
	Route(name='forum_post', method='GET', path=UrlPath(original='/api/v1/json/forums/:short_name/topics/:topic_slug/posts/:post_id', template='/api/v1/json/forums/{short_name}/topics/{topic_slug}/posts/{post_id}', params=[Parameter(name='short_name', type='String', description='the variable short_name part of the url.', optional=False), Parameter(name='topic_slug', type='String', description='the variable topic_slug part of the url.', optional=False), Parameter(name='post_id', type='Integer', description='the variable post_id part of the url.', optional=False)]), allowed_query_parameters=[], description='Fetches a **post response** for the abbreviated forum name given by the `short_name`, topic given by `topic_slug` and post given by `post_id` URL parameters.', response_format=ResponseType(schema='{"post":Post}', is_list=False, key='post', class_name='Post'), example_url='/api/v1/json/forums/dis/topics/ask-the-mods-anything/posts/2761095'),
]
classes = [
	Class(name='Intensities', params=[Parameter(name='ne', type='Float', description='Northeast intensity. Whatever that means…', optional=False), Parameter(name='nw', type='Float', description='Northwest intensity. Whatever that means…', optional=False), Parameter(name='se', type='Float', description='Southeast intensity. Whatever that means…', optional=False), Parameter(name='sw', type='Float', description='Southwest intensity. Whatever that means…', optional=False)]),
	Class(name='Representations', params=[Parameter(name='full', type='String', description="A mapping of the 'full' representation names to their respective URLs.", optional=False), Parameter(name='large', type='String', description="A mapping of the 'large' representation names to their respective URLs.", optional=False), Parameter(name='medium', type='String', description="A mapping of the 'medium' representation names to their respective URLs.", optional=False), Parameter(name='small', type='String', description="A mapping of the 'small' representation names to their respective URLs.", optional=False), Parameter(name='tall', type='String', description="A mapping of the 'tall' representation names to their respective URLs.", optional=False), Parameter(name='thumb', type='String', description="A mapping of the 'thumb' representation names to their respective URLs.", optional=False), Parameter(name='thumb_small', type='String', description="A mapping of the 'thumb_small' representation names to their respective URLs.", optional=False), Parameter(name='thumb_tiny', type='String', description="A mapping of the 'thumb_tiny' representation names to their respective URLs.", optional=False)]),
	Class(name='Image', params=[Parameter(name='aspect_ratio', type='Float', description="The image's width divided by its height.", optional=False), Parameter(name='comment_count', type='Integer', description='The number of comments made on the image.', optional=False), Parameter(name='created_at', type='RFC3339 datetime', description='The creation time, in UTC, of the image.', optional=False), Parameter(name='deletion_reason', type='String', description='The hide reason for the image, or null if none provided. This will only have a value on images which are deleted for a rule violation.', optional=False), Parameter(name='description', type='String', description="The image's description.", optional=False), Parameter(name='downvotes', type='Integer', description='The number of downvotes the image has.', optional=False), Parameter(name='duplicate_of', type='Integer', description='The ID of the target image, or null if none provided. This will only have a value on images which are merged into another image.', optional=False), Parameter(name='faves', type='Integer', description='The number of faves the image has.', optional=False), Parameter(name='first_seen_at', type='RFC3339 datetime', description='The time, in UTC, this image was first seen (before any duplicate merging).', optional=False), Parameter(name='format', type='String', description='The file extension of this image. One of "gif", "jpg", "jpeg", "png", "svg", "webm".', optional=False), Parameter(name='height', type='Integer', description="The image's height, in pixels.", optional=False), Parameter(name='hidden_from_users', type='Boolean', description='Whether this image is hidden. An image is hidden if it is merged or deleted for a rule violation.', optional=False), Parameter(name='id', type='Integer', description="The image's ID.", optional=False), Parameter(name='intensities', type='`Intensities`', description='Optional object of internal image intensity data for deduplication purposes. May be null if intensities have not yet been generated.', optional=False), Parameter(name='mime_type', type='String', description='The MIME type of this image. One of "image/gif", "image/jpeg", "image/png", "image/svg+xml", "video/webm".', optional=False), Parameter(name='name', type='String', description='The filename that this image was uploaded with.', optional=False), Parameter(name='orig_sha512_hash', type='String', description='The SHA512 hash of this image as it was originally uploaded.', optional=False), Parameter(name='processed', type='Boolean', description='Whether the image has finished optimization.', optional=False), Parameter(name='representations', type='Representations', description='A mapping of representation names to their respective URLs. Contains the keys "full", "large", "medium", "small", "tall", "thumb", "thumb_small", "thumb_tiny".', optional=False), Parameter(name='score', type='Integer', description="The image's number of upvotes minus the image's number of downvotes.", optional=False), Parameter(name='sha512_hash', type='String', description='The SHA512 hash of this image after it has been processed.', optional=False), Parameter(name='source_url', type='String', description='The current source URL of the image.', optional=False), Parameter(name='spoilered', type='Boolean', description='Whether this image is hit by the current filter.', optional=False), Parameter(name='tag_count', type='Integer', description='The number of tags present on this image.', optional=False), Parameter(name='tag_ids', type='Array', description='A list of tag IDs this image contains.', optional=False), Parameter(name='tags', type='Array', description='A list of tag names this image contains.', optional=False), Parameter(name='thumbnails_generated', type='Boolean', description='Whether this image has finished thumbnail generation. Do not attempt to load images from view_url or representations if this is false.', optional=False), Parameter(name='updated_at', type='RFC3339 datetime', description='The time, in UTC, the image was last updated.', optional=False), Parameter(name='uploader', type='String', description="The image's uploader.", optional=False), Parameter(name='uploader_id', type='Integer', description="The ID of the image's uploader.", optional=False), Parameter(name='upvotes', type='Integer', description="The image's number of upvotes.", optional=False), Parameter(name='view_url', type='String', description="The image's view URL, including tags.", optional=False), Parameter(name='width', type='Integer', description="The image's width, in pixels.", optional=False), Parameter(name='wilson_score', type='Float', description='The lower bound of the Wilson score interval for the image, based on its upvotes and downvotes, given a z-score corresponding to a confidence of 99.5%.', optional=False)]),
	Class(name='Comment', params=[Parameter(name='author', type='String', description="The comment's author.", optional=False), Parameter(name='body', type='String', description='The comment text.', optional=False), Parameter(name='id', type='Integer', description="The comment's ID.", optional=False), Parameter(name='image_id', type='Integer', description='The ID of the image the comment belongs to.', optional=False), Parameter(name='user_id', type='Integer', description='The ID of the user the comment belongs to, if any.', optional=False)]),
	Class(name='Forum', params=[Parameter(name='name', type='String', description="The forum's name.", optional=False), Parameter(name='short_name', type='String', description="The forum's short name (used to identify it).", optional=False), Parameter(name='description', type='String', description="The forum's description.", optional=False), Parameter(name='topic_count', type='Integer', description='The amount of topics in the forum.', optional=False), Parameter(name='post_count', type='Integer', description='The amount of posts in the forum.', optional=False)]),
	Class(name='Topic', params=[Parameter(name='slug', type='String', description="The topic's slug (used to identify it).", optional=False), Parameter(name='title', type='String', description="The topic's title.", optional=False), Parameter(name='post_count', type='Integer', description='The amount of posts in the topic.', optional=False), Parameter(name='view_count', type='Integer', description='The amount of views the topic has received.', optional=False), Parameter(name='sticky', type='Boolean', description='Whether the topic is sticky.', optional=False), Parameter(name='last_replied_to_at', type='RFC3339 datetime', description='The time, in UTC, when the last reply was made.', optional=False), Parameter(name='locked', type='Boolean', description='Whether the topic is locked.', optional=False), Parameter(name='user_id', type='Integer', description='The ID of the user who made the topic. Null if posted anonymously.', optional=False), Parameter(name='author', type='String', description='The name of the user who made the topic.', optional=False)]),
	Class(name='Post', params=[Parameter(name='author', type='String', description="The post's author.", optional=False), Parameter(name='body', type='String', description='The post text.', optional=False), Parameter(name='id', type='Integer', description="The post's ID (used to identify it).", optional=False), Parameter(name='user_id', type='Integer', description='The ID of the user the comment belongs to, if any.', optional=False)]),
	Class(name='Tag', params=[Parameter(name='aliased_tag', type='String', description='The slug of the tag this tag is aliased to, if any.', optional=False), Parameter(name='aliases', type='Array', description='The slugs of the tags aliased to this tag.', optional=False), Parameter(name='category', type='String', description='The category class of this tag. One of "character", "content-fanmade", "content-official", "error", "oc", "origin", "rating", "species", "spoiler".', optional=False), Parameter(name='description', type='String', description='The long description for the tag.', optional=False), Parameter(name='dnp_entries', type='Array', description='An array of objects containing DNP entries claimed on the tag.', optional=False), Parameter(name='id', type='Integer', description="The tag's ID.", optional=False), Parameter(name='images', type='Integer', description='The image count of the tag.', optional=False), Parameter(name='implied_by_tags', type='Array', description='The slugs of the tags this tag is implied by.', optional=False), Parameter(name='implied_tags', type='Array', description='The slugs of the tags this tag implies.', optional=False), Parameter(name='name', type='String', description='The name of the tag.', optional=False), Parameter(name='name_in_namespace', type='String', description='The name of the tag in its namespace.', optional=False), Parameter(name='namespace', type='String', description='The namespace of the tag.', optional=False), Parameter(name='short_description', type='String', description='The short description for the tag.', optional=False), Parameter(name='slug', type='String', description='The slug for the tag.', optional=False), Parameter(name='spoiler_image', type='String', description='The spoiler image URL for the tag.', optional=False)]),
	Class(name='User', params=[Parameter(name='id', type='Integer', description='The ID of the user.', optional=False), Parameter(name='name', type='String', description='The name of the user.', optional=False), Parameter(name='slug', type='String', description='The slug of the user.', optional=False), Parameter(name='role', type='String', description='The role of the user.', optional=False), Parameter(name='description', type='String', description='The description (bio) of the user.', optional=False), Parameter(name='avatar_url', type='String', description="The URL of the user's thumbnail. Null if they haven't set one.", optional=False), Parameter(name='created_at', type='RFC3339 datetime', description='The creation time, in UTC, of the user.', optional=False), Parameter(name='comments_count', type='Integer', description='The comment count of the user.', optional=False), Parameter(name='uploads_count', type='Integer', description='The upload count of the user.', optional=False), Parameter(name='posts_count', type='Integer', description='The forum posts count of the user.', optional=False), Parameter(name='topics_count', type='Integer', description='The forum topics count of the user.', optional=False), Parameter(name='links', type='`Links`', description='The links the user has registered. See `Links`.', optional=False), Parameter(name='awards', type='`Awards`', description='The awards/badges of the user. See `Awards`.', optional=False)]),
	Class(name='Filter', params=[Parameter(name='id', type='Integer', description='The id of the filter.', optional=False), Parameter(name='name', type='String', description='The name of the filter.', optional=False), Parameter(name='description', type='String', description='The description of the filter.', optional=False), Parameter(name='user_id', type='Integer', description="The id of the user the filter belongs to. Null if it isn't assigned to a user (usually system filters only).", optional=False), Parameter(name='user_count', type='Integer', description='The amount of users employing this filter.', optional=False), Parameter(name='system', type='Boolean', description="If true, is a system filter. System filters are usable by anyone and don't have a user_id set.", optional=False), Parameter(name='public', type='Boolean', description='If true, is a public filter. Public filters are usable by anyone.', optional=False), Parameter(name='spoilered_tag_ids', type='Array', description='A list of tag IDs (as integers) that this filter will spoil.', optional=False), Parameter(name='spoilered_complex', type='String', description='The complex spoiled filter.', optional=False), Parameter(name='hidden_tag_ids', type='Array', description='A list of tag IDs (as integers) that this filter will hide.', optional=False), Parameter(name='hidden_complex', type='String', description='The complex hidden filter.', optional=False)]),
	Class(name='Links', params=[Parameter(name='user_id', type='Integer', description='The ID of the user who owns this link.', optional=False), Parameter(name='created_at', type='RFC3339 datetime', description='The creation time, in UTC, of this link.', optional=False), Parameter(name='state', type='String', description='The state of this link.', optional=False), Parameter(name='tag_id', type='Integer', description='The ID of an associated tag for this link. Null if no tag linked.', optional=False)]),
	Class(name='Awards', params=[Parameter(name='image_url', type='String', description='The URL of this award.', optional=False), Parameter(name='title', type='String', description='The title of this award.', optional=False), Parameter(name='id', type='Integer', description='The ID of the badge this award is derived from.', optional=False), Parameter(name='label', type='String', description='The label of this award.', optional=False), Parameter(name='awarded_on', type='RFC3339 datetime', description='The time, in UTC, when this award was given.', optional=False)]),
	Class(name='Gallery', params=[Parameter(name='description', type='String', description="The gallery's description.", optional=False), Parameter(name='id', type='Integer', description="The gallery's ID.", optional=False), Parameter(name='spoiler_warning', type='String', description="The gallery's spoiler warning.", optional=False), Parameter(name='thumbnail_id', type='Integer', description='The ID of the cover image for the gallery.', optional=False), Parameter(name='title', type='String', description="The gallery's title.", optional=False), Parameter(name='user', type='String', description="The name of the gallery's creator.", optional=False), Parameter(name='user_id', type='Integer', description="The ID of the gallery's creator.", optional=False)]),
	Class(name='Oembed', params=[Parameter(name='author_name', type='String', description='The comma-delimited names of the image authors.', optional=False), Parameter(name='author_url', type='String', description='The source URL of the image.', optional=False), Parameter(name='cache_age', type='Integer', description='Always 7200.', optional=False), Parameter(name='derpibooru_comments', type='Integer', description='The number of comments made on the image.', optional=False), Parameter(name='derpibooru_id', type='Integer', description="The image's ID.", optional=False), Parameter(name='derpibooru_score', type='Integer', description="The image's number of upvotes minus the image's number of downvotes.", optional=False), Parameter(name='derpibooru_tags', type='Array', description="The names of the image's tags.", optional=False), Parameter(name='provider_name', type='String', description='Always "Derpibooru".', optional=False), Parameter(name='provider_url', type='String', description='Always "https://derpibooru.org".', optional=False), Parameter(name='title', type='String', description="The image's ID and associated tags, as would be given on the title of the image page.", optional=False), Parameter(name='type', type='String', description='Always "photo".', optional=False), Parameter(name='version', type='String', description='Always "1.0".', optional=False)]),
]
