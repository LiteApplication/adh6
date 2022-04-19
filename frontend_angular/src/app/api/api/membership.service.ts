/**
 * ADH6 API
 * This is the specification for **MiNET**'s ADH6 plaform. Its aim is to manage our users, devices and treasury. 
 *
 * OpenAPI spec version: 2.0.0
 * Contact: equipe@minet.net
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 *//* tslint:disable:no-unused-variable member-ordering */

import { Inject, Injectable, Optional }                      from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams,
         HttpResponse, HttpEvent }                           from '@angular/common/http';
import { CustomHttpUrlEncodingCodec }                        from '../encoder';

import { Observable }                                        from 'rxjs';

import { AbstractMembership } from '../model/abstractMembership';
import { Membership } from '../model/membership';

import { BASE_PATH, COLLECTION_FORMATS }                     from '../variables';
import { Configuration }                                     from '../configuration';


@Injectable()
export class MembershipService {

    protected basePath = 'https://adh6.minet.net/api/';
    public defaultHeaders = new HttpHeaders();
    public configuration = new Configuration();

    constructor(protected httpClient: HttpClient, @Optional()@Inject(BASE_PATH) basePath: string, @Optional() configuration: Configuration) {
        if (basePath) {
            this.basePath = basePath;
        }
        if (configuration) {
            this.configuration = configuration;
            this.basePath = basePath || configuration.basePath || this.basePath;
        }
    }

    /**
     * @param consumes string[] mime-types
     * @return true: consumes contains 'multipart/form-data', false: otherwise
     */
    private canConsumeForm(consumes: string[]): boolean {
        const form = 'multipart/form-data';
        for (const consume of consumes) {
            if (form === consume) {
                return true;
            }
        }
        return false;
    }


    /**
     * Get the latest pending membership of a specific member
     * 
     * @param id The id of the account that needs to be fetched.
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     * @param criticalError flag to set whether an error on this request should me considered critical for the application flow
     */
    public getLatestMembership(id: number, observe?: 'body', reportProgress?: boolean, criticalError?: boolean): Observable<Membership>;
    public getLatestMembership(id: number, observe?: 'response', reportProgress?: boolean, criticalError?: boolean): Observable<HttpResponse<Membership>>;
    public getLatestMembership(id: number, observe?: 'events', reportProgress?: boolean, criticalError?: boolean): Observable<HttpEvent<Membership>>;
    public getLatestMembership(id: number, observe: any = 'body', reportProgress: boolean = false, criticalError: boolean = true ): Observable<any> {

        if (id === null || id === undefined) {
            throw new Error('Required parameter id was null or undefined when calling getLatestMembership.');
        }

        let headers = this.defaultHeaders;

        // authentication (ApiKeyAuth) required
        if (this.configuration.apiKeys["X-API-KEY"]) {
            headers = headers.set('X-API-KEY', this.configuration.apiKeys["X-API-KEY"]);
        }

        // authentication (OAuth2) required
        if (this.configuration.accessToken) {
            const accessToken = typeof this.configuration.accessToken === 'function'
                ? this.configuration.accessToken()
                : this.configuration.accessToken;
            headers = headers.set('Authorization', 'Bearer ' + accessToken);
        }

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        headers = headers.set('X-Critical-Error', ''+criticalError);
        return this.httpClient.request<Membership>('get',`${this.basePath}/member/${encodeURIComponent(String(id))}/membership/`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Add a membership record for a member
     * 
     * @param body The membership to create
     * @param id The id of the account that needs to be fetched.
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     * @param criticalError flag to set whether an error on this request should me considered critical for the application flow
     */
    public memberIdMembershipPost(body: Membership, id: number, observe?: 'body', reportProgress?: boolean, criticalError?: boolean): Observable<Membership>;
    public memberIdMembershipPost(body: Membership, id: number, observe?: 'response', reportProgress?: boolean, criticalError?: boolean): Observable<HttpResponse<Membership>>;
    public memberIdMembershipPost(body: Membership, id: number, observe?: 'events', reportProgress?: boolean, criticalError?: boolean): Observable<HttpEvent<Membership>>;
    public memberIdMembershipPost(body: Membership, id: number, observe: any = 'body', reportProgress: boolean = false, criticalError: boolean = true ): Observable<any> {

        if (body === null || body === undefined) {
            throw new Error('Required parameter body was null or undefined when calling memberIdMembershipPost.');
        }

        if (id === null || id === undefined) {
            throw new Error('Required parameter id was null or undefined when calling memberIdMembershipPost.');
        }

        let headers = this.defaultHeaders;

        // authentication (ApiKeyAuth) required
        if (this.configuration.apiKeys["X-API-KEY"]) {
            headers = headers.set('X-API-KEY', this.configuration.apiKeys["X-API-KEY"]);
        }

        // authentication (OAuth2) required
        if (this.configuration.accessToken) {
            const accessToken = typeof this.configuration.accessToken === 'function'
                ? this.configuration.accessToken()
                : this.configuration.accessToken;
            headers = headers.set('Authorization', 'Bearer ' + accessToken);
        }

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
            'application/json'
        ];
        const httpContentTypeSelected: string | undefined = this.configuration.selectHeaderContentType(consumes);
        if (httpContentTypeSelected != undefined) {
            headers = headers.set('Content-Type', httpContentTypeSelected);
        }

        headers = headers.set('X-Critical-Error', ''+criticalError);
        return this.httpClient.request<Membership>('post',`${this.basePath}/member/${encodeURIComponent(String(id))}/membership/`,
            {
                body: body,
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Retrieve a membership
     * 
     * @param id The id of the account that needs to be fetched.
     * @param uuid The UUID associated with this membership request
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     * @param criticalError flag to set whether an error on this request should me considered critical for the application flow
     */
    public memberIdMembershipUuidGet(id: number, uuid: string, observe?: 'body', reportProgress?: boolean, criticalError?: boolean): Observable<Membership>;
    public memberIdMembershipUuidGet(id: number, uuid: string, observe?: 'response', reportProgress?: boolean, criticalError?: boolean): Observable<HttpResponse<Membership>>;
    public memberIdMembershipUuidGet(id: number, uuid: string, observe?: 'events', reportProgress?: boolean, criticalError?: boolean): Observable<HttpEvent<Membership>>;
    public memberIdMembershipUuidGet(id: number, uuid: string, observe: any = 'body', reportProgress: boolean = false, criticalError: boolean = true ): Observable<any> {

        if (id === null || id === undefined) {
            throw new Error('Required parameter id was null or undefined when calling memberIdMembershipUuidGet.');
        }

        if (uuid === null || uuid === undefined) {
            throw new Error('Required parameter uuid was null or undefined when calling memberIdMembershipUuidGet.');
        }

        let headers = this.defaultHeaders;

        // authentication (ApiKeyAuth) required
        if (this.configuration.apiKeys["X-API-KEY"]) {
            headers = headers.set('X-API-KEY', this.configuration.apiKeys["X-API-KEY"]);
        }

        // authentication (OAuth2) required
        if (this.configuration.accessToken) {
            const accessToken = typeof this.configuration.accessToken === 'function'
                ? this.configuration.accessToken()
                : this.configuration.accessToken;
            headers = headers.set('Authorization', 'Bearer ' + accessToken);
        }

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        headers = headers.set('X-Critical-Error', ''+criticalError);
        return this.httpClient.request<Membership>('get',`${this.basePath}/member/${encodeURIComponent(String(id))}/membership/${encodeURIComponent(String(uuid))}`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Partially update a membership
     * 
     * @param body The new values for this member
     * @param id The id of the account that needs to be fetched.
     * @param uuid The UUID associated with this membership request
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     * @param criticalError flag to set whether an error on this request should me considered critical for the application flow
     */
    public memberIdMembershipUuidPatch(body: AbstractMembership, id: number, uuid: string, observe?: 'body', reportProgress?: boolean, criticalError?: boolean): Observable<any>;
    public memberIdMembershipUuidPatch(body: AbstractMembership, id: number, uuid: string, observe?: 'response', reportProgress?: boolean, criticalError?: boolean): Observable<HttpResponse<any>>;
    public memberIdMembershipUuidPatch(body: AbstractMembership, id: number, uuid: string, observe?: 'events', reportProgress?: boolean, criticalError?: boolean): Observable<HttpEvent<any>>;
    public memberIdMembershipUuidPatch(body: AbstractMembership, id: number, uuid: string, observe: any = 'body', reportProgress: boolean = false, criticalError: boolean = true ): Observable<any> {

        if (body === null || body === undefined) {
            throw new Error('Required parameter body was null or undefined when calling memberIdMembershipUuidPatch.');
        }

        if (id === null || id === undefined) {
            throw new Error('Required parameter id was null or undefined when calling memberIdMembershipUuidPatch.');
        }

        if (uuid === null || uuid === undefined) {
            throw new Error('Required parameter uuid was null or undefined when calling memberIdMembershipUuidPatch.');
        }

        let headers = this.defaultHeaders;

        // authentication (ApiKeyAuth) required
        if (this.configuration.apiKeys["X-API-KEY"]) {
            headers = headers.set('X-API-KEY', this.configuration.apiKeys["X-API-KEY"]);
        }

        // authentication (OAuth2) required
        if (this.configuration.accessToken) {
            const accessToken = typeof this.configuration.accessToken === 'function'
                ? this.configuration.accessToken()
                : this.configuration.accessToken;
            headers = headers.set('Authorization', 'Bearer ' + accessToken);
        }

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
            'application/json'
        ];
        const httpContentTypeSelected: string | undefined = this.configuration.selectHeaderContentType(consumes);
        if (httpContentTypeSelected != undefined) {
            headers = headers.set('Content-Type', httpContentTypeSelected);
        }

        headers = headers.set('X-Critical-Error', ''+criticalError);
        return this.httpClient.request<any>('patch',`${this.basePath}/member/${encodeURIComponent(String(id))}/membership/${encodeURIComponent(String(uuid))}`,
            {
                body: body,
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Filter memberships
     * 
     * @param limit Limit the number of results returned
     * @param offset Skip the first n results
     * @param terms The generic search terms (will search in any field)
     * @param filter Filters by various properties
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     * @param criticalError flag to set whether an error on this request should me considered critical for the application flow
     */
    public membershipSearch(limit?: number, offset?: number, terms?: string, filter?: any, observe?: 'body', reportProgress?: boolean, criticalError?: boolean): Observable<Array<Membership>>;
    public membershipSearch(limit?: number, offset?: number, terms?: string, filter?: any, observe?: 'response', reportProgress?: boolean, criticalError?: boolean): Observable<HttpResponse<Array<Membership>>>;
    public membershipSearch(limit?: number, offset?: number, terms?: string, filter?: any, observe?: 'events', reportProgress?: boolean, criticalError?: boolean): Observable<HttpEvent<Array<Membership>>>;
    public membershipSearch(limit?: number, offset?: number, terms?: string, filter?: any, observe: any = 'body', reportProgress: boolean = false, criticalError: boolean = true ): Observable<any> {





        let queryParameters = new HttpParams({encoder: new CustomHttpUrlEncodingCodec()});
        if (limit !== undefined && limit !== null) {
            queryParameters = queryParameters.set('limit', <any>limit);
        }
        if (offset !== undefined && offset !== null) {
            queryParameters = queryParameters.set('offset', <any>offset);
        }
        if (terms !== undefined && terms !== null) {
            queryParameters = queryParameters.set('terms', <any>terms);
        }
        if (filter) {
            for (const key in filter) {
                if (Object.prototype.hasOwnProperty.call(filter, key)) {
                  const value = filter[key];
                  queryParameters = queryParameters.append('filter[' + key + ']', <any>value);
                }
            }
        }

        let headers = this.defaultHeaders;

        // authentication (ApiKeyAuth) required
        if (this.configuration.apiKeys["X-API-KEY"]) {
            headers = headers.set('X-API-KEY', this.configuration.apiKeys["X-API-KEY"]);
        }

        // authentication (OAuth2) required
        if (this.configuration.accessToken) {
            const accessToken = typeof this.configuration.accessToken === 'function'
                ? this.configuration.accessToken()
                : this.configuration.accessToken;
            headers = headers.set('Authorization', 'Bearer ' + accessToken);
        }

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        headers = headers.set('X-Critical-Error', ''+criticalError);
        return this.httpClient.request<Array<Membership>>('get',`${this.basePath}/member/membership/`,
            {
                params: queryParameters,
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Validate a pending transaction
     * 
     * @param id The id of the account that needs to be fetched.
     * @param uuid The UUID associated with this membership request
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     * @param criticalError flag to set whether an error on this request should me considered critical for the application flow
     */
    public membershipValidate(id: number, uuid: string, observe?: 'body', reportProgress?: boolean, criticalError?: boolean): Observable<any>;
    public membershipValidate(id: number, uuid: string, observe?: 'response', reportProgress?: boolean, criticalError?: boolean): Observable<HttpResponse<any>>;
    public membershipValidate(id: number, uuid: string, observe?: 'events', reportProgress?: boolean, criticalError?: boolean): Observable<HttpEvent<any>>;
    public membershipValidate(id: number, uuid: string, observe: any = 'body', reportProgress: boolean = false, criticalError: boolean = true ): Observable<any> {

        if (id === null || id === undefined) {
            throw new Error('Required parameter id was null or undefined when calling membershipValidate.');
        }

        if (uuid === null || uuid === undefined) {
            throw new Error('Required parameter uuid was null or undefined when calling membershipValidate.');
        }

        let headers = this.defaultHeaders;

        // authentication (ApiKeyAuth) required
        if (this.configuration.apiKeys["X-API-KEY"]) {
            headers = headers.set('X-API-KEY', this.configuration.apiKeys["X-API-KEY"]);
        }

        // authentication (OAuth2) required
        if (this.configuration.accessToken) {
            const accessToken = typeof this.configuration.accessToken === 'function'
                ? this.configuration.accessToken()
                : this.configuration.accessToken;
            headers = headers.set('Authorization', 'Bearer ' + accessToken);
        }

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        headers = headers.set('X-Critical-Error', ''+criticalError);
        return this.httpClient.request<any>('get',`${this.basePath}/member/${encodeURIComponent(String(id))}/membership/${encodeURIComponent(String(uuid))}/validate`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

}
