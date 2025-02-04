# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import functools
import re
from typing import Dict, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.cloud.datacatalog_v1.types import policytagmanager
from google.cloud.datacatalog_v1.types import policytagmanagerserialization
from google.cloud.datacatalog_v1.types import timestamps
from .transports.base import PolicyTagManagerSerializationTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import PolicyTagManagerSerializationGrpcAsyncIOTransport
from .client import PolicyTagManagerSerializationClient


class PolicyTagManagerSerializationAsyncClient:
    """Policy Tag Manager Serialization API service allows you to
    manipulate your policy tags and taxonomies in a serialized
    format.
    Taxonomy is a hierarchical group of policy tags.
    """

    _client: PolicyTagManagerSerializationClient

    DEFAULT_ENDPOINT = PolicyTagManagerSerializationClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = PolicyTagManagerSerializationClient.DEFAULT_MTLS_ENDPOINT

    taxonomy_path = staticmethod(PolicyTagManagerSerializationClient.taxonomy_path)
    parse_taxonomy_path = staticmethod(
        PolicyTagManagerSerializationClient.parse_taxonomy_path
    )
    common_billing_account_path = staticmethod(
        PolicyTagManagerSerializationClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        PolicyTagManagerSerializationClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(
        PolicyTagManagerSerializationClient.common_folder_path
    )
    parse_common_folder_path = staticmethod(
        PolicyTagManagerSerializationClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        PolicyTagManagerSerializationClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        PolicyTagManagerSerializationClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        PolicyTagManagerSerializationClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        PolicyTagManagerSerializationClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        PolicyTagManagerSerializationClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        PolicyTagManagerSerializationClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            PolicyTagManagerSerializationAsyncClient: The constructed client.
        """
        return PolicyTagManagerSerializationClient.from_service_account_info.__func__(PolicyTagManagerSerializationAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            PolicyTagManagerSerializationAsyncClient: The constructed client.
        """
        return PolicyTagManagerSerializationClient.from_service_account_file.__func__(PolicyTagManagerSerializationAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return PolicyTagManagerSerializationClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> PolicyTagManagerSerializationTransport:
        """Returns the transport used by the client instance.

        Returns:
            PolicyTagManagerSerializationTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(PolicyTagManagerSerializationClient).get_transport_class,
        type(PolicyTagManagerSerializationClient),
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, PolicyTagManagerSerializationTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the policy tag manager serialization client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.PolicyTagManagerSerializationTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = PolicyTagManagerSerializationClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def replace_taxonomy(
        self,
        request: Union[
            policytagmanagerserialization.ReplaceTaxonomyRequest, dict
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> policytagmanager.Taxonomy:
        r"""Replaces (updates) a taxonomy and all its policy tags.

        The taxonomy and its entire hierarchy of policy tags must be
        represented literally by ``SerializedTaxonomy`` and the nested
        ``SerializedPolicyTag`` messages.

        This operation automatically does the following:

        -  Deletes the existing policy tags that are missing from the
           ``SerializedPolicyTag``.
        -  Creates policy tags that don't have resource names. They are
           considered new.
        -  Updates policy tags with valid resources names accordingly.

        Args:
            request (Union[google.cloud.datacatalog_v1.types.ReplaceTaxonomyRequest, dict]):
                The request object. Request message for
                [ReplaceTaxonomy][google.cloud.datacatalog.v1.PolicyTagManagerSerialization.ReplaceTaxonomy].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1.types.Taxonomy:
                A taxonomy is a collection of hierarchical policy tags that classify data
                   along a common axis.

                   For example, a "data sensitivity" taxonomy might
                   contain the following policy tags:

                   :literal:`\` + PII   + Account number   + Age   + SSN   + Zipcode + Financials   + Revenue`\ \`

                   A "data origin" taxonomy might contain the following
                   policy tags:

                   :literal:`\` + User data + Employee data + Partner data + Public data`\ \`

        """
        # Create or coerce a protobuf request object.
        request = policytagmanagerserialization.ReplaceTaxonomyRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.replace_taxonomy,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def import_taxonomies(
        self,
        request: Union[
            policytagmanagerserialization.ImportTaxonomiesRequest, dict
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> policytagmanagerserialization.ImportTaxonomiesResponse:
        r"""Creates new taxonomies (including their policy tags)
        in a given project by importing from inlined or cross-
        regional sources.
        For a cross-regional source, new taxonomies are created
        by copying from a source in another region.

        For an inlined source, taxonomies and policy tags are
        created in bulk using nested protocol buffer structures.

        Args:
            request (Union[google.cloud.datacatalog_v1.types.ImportTaxonomiesRequest, dict]):
                The request object. Request message for
                [ImportTaxonomies][google.cloud.datacatalog.v1.PolicyTagManagerSerialization.ImportTaxonomies].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1.types.ImportTaxonomiesResponse:
                Response message for
                   [ImportTaxonomies][google.cloud.datacatalog.v1.PolicyTagManagerSerialization.ImportTaxonomies].

        """
        # Create or coerce a protobuf request object.
        request = policytagmanagerserialization.ImportTaxonomiesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.import_taxonomies,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def export_taxonomies(
        self,
        request: Union[
            policytagmanagerserialization.ExportTaxonomiesRequest, dict
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> policytagmanagerserialization.ExportTaxonomiesResponse:
        r"""Exports taxonomies in the requested type and returns them,
        including their policy tags. The requested taxonomies must
        belong to the same project.

        This method generates ``SerializedTaxonomy`` protocol buffers
        with nested policy tags that can be used as input for
        ``ImportTaxonomies`` calls.

        Args:
            request (Union[google.cloud.datacatalog_v1.types.ExportTaxonomiesRequest, dict]):
                The request object. Request message for
                [ExportTaxonomies][google.cloud.datacatalog.v1.PolicyTagManagerSerialization.ExportTaxonomies].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.datacatalog_v1.types.ExportTaxonomiesResponse:
                Response message for
                   [ExportTaxonomies][google.cloud.datacatalog.v1.PolicyTagManagerSerialization.ExportTaxonomies].

        """
        # Create or coerce a protobuf request object.
        request = policytagmanagerserialization.ExportTaxonomiesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.export_taxonomies,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-datacatalog",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("PolicyTagManagerSerializationAsyncClient",)
