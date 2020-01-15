/**
 * Adherent
 * Adherent api
 *
 * OpenAPI spec version: 1.0.0
 *
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

import { MembershipRequest } from '../model/membershipRequest';

import { BASE_PATH, COLLECTION_FORMATS }                     from '../variables';
import { Configuration }                                     from '../configuration';


@Injectable()
export class MembershipService {

    protected basePath = '/api';
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
     * Add a membership record for an member
     *
     * @param body Membership record, if no start is specified, it will use the current date. Duration is expressed in days. WARNING: DO NOT set the start date to be in the future, it is not implemented for the moment.
     * @param username The username of the member
     * @param xIdempotencyKey Just a random string to ensure that membership creation is idempotent (very important since double submission may result to the member being charged two times). I recommand using a long random string for that.
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public memberUsernameMembershipPost(body: MembershipRequest, username: string, xIdempotencyKey?: string, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public memberUsernameMembershipPost(body: MembershipRequest, username: string, xIdempotencyKey?: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public memberUsernameMembershipPost(body: MembershipRequest, username: string, xIdempotencyKey?: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public memberUsernameMembershipPost(body: MembershipRequest, username: string, xIdempotencyKey?: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (body === null || body === undefined) {
            throw new Error('Required parameter body was null or undefined when calling memberUsernameMembershipPost.');
        }

        if (username === null || username === undefined) {
            throw new Error('Required parameter username was null or undefined when calling memberUsernameMembershipPost.');
        }


        let headers = this.defaultHeaders;
        if (xIdempotencyKey !== undefined && xIdempotencyKey !== null) {
            headers = headers.set('X-Idempotency-Key', String(xIdempotencyKey));
        }

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
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

        return this.httpClient.request<any>('post',`${this.basePath}/member/${encodeURIComponent(String(username))}/membership/`,
            {
                body: body,
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

}
