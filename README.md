# Django-Rest-Framework-CRUD
JWT Authentication with  drf-yasg


### **What is JWT Authentication?**

JSON Web Token (JWT) is a JSON encoded representation of a claim(s) that can be transferred between two parties. The claim is digitally signed by the issuer of the token, and the party receiving this token can later use this digital signature to prove the ownership on the claim.  
Here are some scenarios where JSON Web Tokens are useful:

-   **Authorization**: This is the most common scenario for using JWT. Once the user is logged in, each subsequent request will include the JWT, allowing the user to access routes, services, and resources that are permitted with that token. Single Sign On is a feature that widely uses JWT nowadays, because of its small overhead and its ability to be easily used across different domains.
    
-   **Information Exchange**: JSON Web Tokens are a good way of securely transmitting information between parties. Because JWTs can be signed—for example, using public/private key pairs—you can be sure the senders are who they say they are. Additionally, as the signature is calculated using the header and the payload, you can also verify that the content hasn't been tampered with.
  
JWTs can be broken down into three parts: header, payload, and signature. Each part is separated from the other by dot (.), and will follow the below  structure:

**Header.Payload.Signature**


### Header

The header  _typically_  consists of two parts: the type of the token, which is JWT, and the signing algorithm being used, such as HMAC SHA256 or RSA.
Then, this JSON is **Base64Url** encoded to form the first part of the JWT.

### Payload

The second part of the token is the payload, which contains the claims. Claims are statements about an entity (typically, the user) and additional data. There are three types of claims:  _registered_,  _public_, and  _private_  claims.

-   [**Registered claims**](https://tools.ietf.org/html/rfc7519#section-4.1): These are a set of predefined claims which are not mandatory but recommended, to provide a set of useful, interoperable claims. Some of them are:  **iss**  (issuer),  **exp**  (expiration time),  **sub**  (subject),  **aud**  (audience), and  [others](https://tools.ietf.org/html/rfc7519#section-4.1).

-   [**Public claims**](https://tools.ietf.org/html/rfc7519#section-4.2): These can be defined at will by those using JWTs. But to avoid collisions they should be defined in the  [IANA JSON Web Token Registry](https://www.iana.org/assignments/jwt/jwt.xhtml)  or be defined as a URI that contains a collision resistant namespace.
    
-   [**Private claims**](https://tools.ietf.org/html/rfc7519#section-4.3): These are the custom claims created to share information between parties that agree on using them and are neither  _registered_  or  _public_  claims.
The payload is then **Base64Url** encoded to form the second part of the JSON Web Token.

### Signature

To create the signature part you have to take the encoded header, the encoded payload, a secret, the algorithm specified in the header, and sign that.

### Putting all together

The output is three Base64-URL strings separated by dots that can be easily passed in HTML and HTTP environments, while being more compact when compared to XML-based standards such as SAML.


There are many benefits to using JWT tokens regardless of the platform. JWT tokens  `base64`  encode all the users claims in their body and can be safely decoded on the client into a stateful object. This is hugely beneficial when compared to alternative opaque tokens which provide zero use to the client app. On login, you immediately have atomic data in the client without additional round trips to the API to poll for user information.

JWT tokens are stateless: there is no need to store or keep track of them server side, which is more scalable horizontally across many servers. They are safe because the private signing key used to grant them is stored server side, any inbound API calls bearing them are simply validated with the private key, guaranteeing they were issued by your Authorization API.

JWT tokens work nicely in Angular, React, and any other client framework. Because they are JSON, you can  `base64`  decode them in the client and bind client UI elements directly to your claims - someone with an admin claim can see an admin menu and a user without that claim will never know the menu exists, if implemented correctly.

Aside from this, a JWT token still behaves in the same way as any bearer token:

-   Issued by Authorization API
-   Stored by client in cookies or local storage
-   Passed to Resource API in  `Authorization`  header

## Bearer Authentication

**Bearer authentication** (also called **token authentication**) is an [HTTP authentication scheme](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication) that involves security tokens called bearer tokens. The name “Bearer authentication” can be understood as “give access to the bearer of this token.” The bearer token is a cryptic string, usually generated by the server in response to a login request. The client must send this token in the `Authorization` header when making requests to protected resources:
The Bearer authentication scheme was originally created as part of [OAuth 2.0](https://swagger.io/docs/specification/authentication/oauth2/) in [RFC 6750](https://tools.ietf.org/html/rfc6750), but is sometimes also used on its own. Similarly to [Basic authentication](https://swagger.io/docs/specification/authentication/basic-authentication/), Bearer authentication should only be used over HTTPS (SSL).

# [drf-yasg - Yet another Swagger generator](https://drf-yasg.readthedocs.io/en/stable/readme.html#id6)

[![Travis CI](https://img.shields.io/travis/axnsan12/drf-yasg/master.svg)](https://travis-ci.org/axnsan12/drf-yasg) [![Codecov](https://img.shields.io/codecov/c/github/axnsan12/drf-yasg/master.svg)](https://codecov.io/gh/axnsan12/drf-yasg) [![ReadTheDocs](https://img.shields.io/readthedocs/drf-yasg.svg)](https://drf-yasg.readthedocs.io/) [![PyPI](https://img.shields.io/pypi/v/drf-yasg.svg)](https://pypi.org/project/drf-yasg/)

Generate  **real**  Swagger/OpenAPI 2.0 specifications from a Django Rest Framework API.

Compatible with

-   **Django Rest Framework**: 3.10, 3.11, 3.12
-   **Django**: 2.2, 3.0, 3.1
-   **Python**: 3.6, 3.7, 3.8, 3.9

Only the latest patch version of each  `major.minor`  series of Python, Django and Django REST Framework is supported.

**Only the latest version of drf-yasg is supported.**  Support of old versions is dropped immediately with the release of a new version. Please do not create issues before upgrading to the latest release available at the time. Regression reports are accepted and will be resolved with a new release as quickly as possible. Removed features will usually go through a deprecation cycle of a few minor releases.

Resources:

-   **Source**:  [https://github.com/axnsan12/drf-yasg/](https://github.com/axnsan12/drf-yasg/)
-   **Documentation**:  [https://drf-yasg.readthedocs.io/](https://drf-yasg.readthedocs.io/)
-   **Changelog**:  [https://drf-yasg.readthedocs.io/en/stable/changelog.html](https://drf-yasg.readthedocs.io/en/stable/changelog.html)
-   **Live demo**:  [https://drf-yasg-demo.herokuapp.com/](https://drf-yasg-demo.herokuapp.com/)

## [OpenAPI 3.0 note](https://drf-yasg.readthedocs.io/en/stable/readme.html#id7)[](https://drf-yasg.readthedocs.io/en/stable/readme.html#openapi-3-0-note "Permalink to this headline")

If you are looking to add Swagger/OpenAPI support to a new project you might want to take a look at  [drf-spectacular](https://github.com/tfranzel/drf-spectacular), which is an actively maintained new library that shares most of the goals of this project, while working with OpenAPI 3.0 schemas.

OpenAPI 3.0 provides a lot more flexibility than 2.0 in the types of API that can be described.  `drf-yasg`  is unlikely to soon, if ever, get support for OpenAPI 3.0.

## [Features](https://drf-yasg.readthedocs.io/en/stable/readme.html#id8)[](https://drf-yasg.readthedocs.io/en/stable/readme.html#features "Permalink to this headline")

-   full support for nested Serializers and Schemas
-   response schemas and descriptions
-   model definitions compatible with codegen tools
-   customization hooks at all points in the spec generation process
-   JSON and YAML format for spec
-   bundles latest version of  [swagger-ui](https://github.com/swagger-api/swagger-ui)  and  [redoc](https://github.com/Rebilly/ReDoc)  for viewing the generated documentation
-   schema view is cacheable out of the box
-   generated Swagger schema can be automatically validated by  [swagger-spec-validator](https://github.com/Yelp/swagger_spec_validator)
-   supports Django REST Framework API versioning with  `URLPathVersioning`  and  `NamespaceVersioning`; other DRF or custom versioning schemes are not currently supported

## [Usage](https://drf-yasg.readthedocs.io/en/stable/readme.html#id10)[](https://drf-yasg.readthedocs.io/en/stable/readme.html#usage "Permalink to this headline")

### [0. Installation](https://drf-yasg.readthedocs.io/en/stable/readme.html#id11)[](https://drf-yasg.readthedocs.io/en/stable/readme.html#installation "Permalink to this headline")

The preferred instalation method is directly from pypi:

    pip install -U drf-yasg

Additionally, if you want to use the built-in validation mechanisms (see  [4. Validation](https://drf-yasg.readthedocs.io/en/stable/readme.html#validation)), you need to install some extra requirements:

    pip install -U drf-yasg[validation]

[drf-yasg Documentation Release 1.20.0 ](https://buildmedia.readthedocs.org/media/pdf/drf-yasg/stable/drf-yasg.pdf)


# django-cors-headers

[![https://img.shields.io/github/workflow/status/adamchainz/django-cors-headers/CI/main?style=for-the-badge](https://camo.githubusercontent.com/430a983b4313a4c77b4df182b976568ad6c74993e9cbf7fe9bf036193e28202e/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f776f726b666c6f772f7374617475732f6164616d636861696e7a2f646a616e676f2d636f72732d686561646572732f43492f6d61696e3f7374796c653d666f722d7468652d6261646765)](https://github.com/adamchainz/django-cors-headers/actions?workflow=CI)  [![https://img.shields.io/codecov/c/github/adamchainz/django-cors-headers/main?style=for-the-badge](https://camo.githubusercontent.com/b7e5f4d2b7fcc9a659fb5fbc7e606db0a4942d705e209022edc4bc631ec2f735/68747470733a2f2f696d672e736869656c64732e696f2f636f6465636f762f632f6769746875622f6164616d636861696e7a2f646a616e676f2d636f72732d686561646572732f6d61696e3f7374796c653d666f722d7468652d6261646765)](https://app.codecov.io/gh/adamchainz/django-cors-headers)  [![https://img.shields.io/pypi/v/django-cors-headers.svg?style=for-the-badge](https://camo.githubusercontent.com/eed5e4f18853a9c736f219a6a953d88ff7b98645e63b65a719932677e4621d19/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f646a616e676f2d636f72732d686561646572732e7376673f7374796c653d666f722d7468652d6261646765)](https://pypi.org/project/django-cors-headers/)  [![https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge](https://camo.githubusercontent.com/1569feb242dfbded0823d577fe848bc86449814507700b2758489815027ecf7a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64652532307374796c652d626c61636b2d3030303030302e7376673f7374796c653d666f722d7468652d6261646765)](https://github.com/psf/black)  [![pre-commit](https://camo.githubusercontent.com/a52ac4000cb1e151c85dbd80bc35132638c07f9529fa54388e5d8fac5c904843/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f7072652d2d636f6d6d69742d656e61626c65642d627269676874677265656e3f6c6f676f3d7072652d636f6d6d6974266c6f676f436f6c6f723d7768697465267374796c653d666f722d7468652d6261646765)](https://github.com/pre-commit/pre-commit)

A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses. This allows in-browser requests to your Django application from other origins.

## [](https://github.com/adamchainz/django-cors-headers#about-cors)About CORS

Cross-origin resource sharing (CORS) is a mechanism that allows many resources (e.g. fonts, JavaScript, etc.) on a web page to be requested from another domain outside the domain from which the resource originated.

Adding CORS headers allows your resources to be accessed on other domains. It's important you understand the implications before adding the headers, since you could be unintentionally opening up your site's private data to others.

### Why do we need CORS?

Because of the same-origin policy. This is a security concept implemented in all modern browsers, which prevent a website from loading data from another website.



Some good resources to read on the subject are:

-   Julia Evans'  [introductory comic](https://drawings.jvns.ca/cors/)  and  [educational quiz](https://questions.wizardzines.com/cors.html).
-   The  [Wikipedia Page](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing)
-   The  [MDN Article](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
-   The  [HTML5 Rocks Tutorial](https://www.html5rocks.com/en/tutorials/cors/)

## [](https://github.com/adamchainz/django-cors-headers#requirements)Requirements

Python 3.6 to 3.9 supported.

Django 2.2 to 3.2 supported.

## Setup

Install from  **pip**:

python -m pip install django-cors-headers

and then add it to your installed apps:

INSTALLED_APPS = [
    ...,
    "corsheaders",
    ...,
]
### So, how does it works?

Some people mistakenly think that allowing CORS is a frontend task when it’s actually implemented in the backend. Frontend developers do not have to perform special requests to access cross origin data. When a browser sends a request to a server it automatically sets some HTTP headers like the “Origin” header that tells the server from which site the request came from.  
Knowing the origin, the server can block the request if it's unauthorized or set the proper headers so the browser knows the request was accepted. As we can see, CORS is an agreement between the browser and the server that does not involves the client application.  
It’s also worth noticing that CORS has no effect on clients outside from the browser since they won't prevent the access of requested data by the application.

#### Some important notes:

-   There are a couple other configurations in the Django CORS headers lib that you can use to adapt it to your needs.
-   Unless you really know what your are doing, never enable CORS to the whole website, this is a serious security flaw.
-   Allowing CORS and using session cookie authentication in your API is also a security flaw. Instead, use something else like a token based authentication.
