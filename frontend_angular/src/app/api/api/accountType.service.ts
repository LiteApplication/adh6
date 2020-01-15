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

import { AccountType } from '../model/accountType';
import { AccountTypePatchRequest } from '../model/accountTypePatchRequest';

import { BASE_PATH, COLLECTION_FORMATS }                     from '../variables';
import { Configuration }                                     from '../configuration';


@Injectable()
export class AccountTypeService {

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
     * Retrieve an account type
     *
     * @param accountTypeId
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public accountTypeAccountTypeIdGet(accountTypeId: number, observe?: 'body', reportProgress?: boolean): Observable<AccountType>;
    public accountTypeAccountTypeIdGet(accountTypeId: number, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<AccountType>>;
    public accountTypeAccountTypeIdGet(accountTypeId: number, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<AccountType>>;
    public accountTypeAccountTypeIdGet(accountTypeId: number, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (accountTypeId === null || accountTypeId === undefined) {
            throw new Error('Required parameter accountTypeId was null or undefined when calling accountTypeAccountTypeIdGet.');
        }

        let headers = this.defaultHeaders;

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

        return this.httpClient.request<AccountType>('get',`${this.basePath}/account_type/${encodeURIComponent(String(accountTypeId))}`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Partially update
     *
     * @param body New values of the account type
     * @param accountTypeId Name of the account type will be updated
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public accountTypeAccountTypeIdPatch(body: AccountTypePatchRequest, accountTypeId: string, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public accountTypeAccountTypeIdPatch(body: AccountTypePatchRequest, accountTypeId: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public accountTypeAccountTypeIdPatch(body: AccountTypePatchRequest, accountTypeId: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public accountTypeAccountTypeIdPatch(body: AccountTypePatchRequest, accountTypeId: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (body === null || body === undefined) {
            throw new Error('Required parameter body was null or undefined when calling accountTypeAccountTypeIdPatch.');
        }

        if (accountTypeId === null || accountTypeId === undefined) {
            throw new Error('Required parameter accountTypeId was null or undefined when calling accountTypeAccountTypeIdPatch.');
        }

        let headers = this.defaultHeaders;

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

        return this.httpClient.request<any>('patch',`${this.basePath}/account_type/${encodeURIComponent(String(accountTypeId))}`,
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
     * Filter account types
     *
     * @param limit Limit the number of account types returned in the result. Default is 100
     * @param offset Skip the first n results
     * @param terms Search terms
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public accountTypeGet(limit?: number, offset?: number, terms?: string, observe?: 'body', reportProgress?: boolean): Observable<Array<AccountType>>;
    public accountTypeGet(limit?: number, offset?: number, terms?: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<Array<AccountType>>>;
    public accountTypeGet(limit?: number, offset?: number, terms?: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<Array<AccountType>>>;
    public accountTypeGet(limit?: number, offset?: number, terms?: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {




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

        let headers = this.defaultHeaders;

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

        return this.httpClient.request<Array<AccountType>>('get',`${this.basePath}/account_type/`,
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
     * Create an account type
     *
     * @param body Account type to create
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public accountTypePost(body: AccountType, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public accountTypePost(body: AccountType, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public accountTypePost(body: AccountType, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public accountTypePost(body: AccountType, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (body === null || body === undefined) {
            throw new Error('Required parameter body was null or undefined when calling accountTypePost.');
        }

        let headers = this.defaultHeaders;

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

        return this.httpClient.request<any>('post',`${this.basePath}/account_type/`,
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
