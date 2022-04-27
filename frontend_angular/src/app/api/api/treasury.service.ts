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

import { Bank } from '../model/bank';
import { Cashbox } from '../model/cashbox';
import { Product } from '../model/product';

import { BASE_PATH, COLLECTION_FORMATS }                     from '../variables';
import { Configuration }                                     from '../configuration';


@Injectable()
export class TreasuryService {

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
     * Retrieve the expected state of MiNET&#x27;s bank accounts
     * 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     * @param criticalError flag to set whether an error on this request should me considered critical for the application flow
     */
    public getBank(observe?: 'body', reportProgress?: boolean, criticalError?: boolean): Observable<Bank>;
    public getBank(observe?: 'response', reportProgress?: boolean, criticalError?: boolean): Observable<HttpResponse<Bank>>;
    public getBank(observe?: 'events', reportProgress?: boolean, criticalError?: boolean): Observable<HttpEvent<Bank>>;
    public getBank(observe: any = 'body', reportProgress: boolean = false, criticalError: boolean = true ): Observable<any> {

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
        return this.httpClient.request<Bank>('get',`${this.basePath}/treasury/bank`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Retrieve the state of the cashbox
     * 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     * @param criticalError flag to set whether an error on this request should me considered critical for the application flow
     */
    public getCashbox(observe?: 'body', reportProgress?: boolean, criticalError?: boolean): Observable<Cashbox>;
    public getCashbox(observe?: 'response', reportProgress?: boolean, criticalError?: boolean): Observable<HttpResponse<Cashbox>>;
    public getCashbox(observe?: 'events', reportProgress?: boolean, criticalError?: boolean): Observable<HttpEvent<Cashbox>>;
    public getCashbox(observe: any = 'body', reportProgress: boolean = false, criticalError: boolean = true ): Observable<any> {

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
        return this.httpClient.request<Cashbox>('get',`${this.basePath}/treasury/cashbox`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Filter products
     * 
     * @param limit Limit the number of results returned
     * @param offset Skip the first n results
     * @param terms The generic search terms (will search in any field)
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     * @param criticalError flag to set whether an error on this request should me considered critical for the application flow
     */
    public productGet(limit?: number, offset?: number, terms?: string, observe?: 'body', reportProgress?: boolean, criticalError?: boolean): Observable<Array<Product>>;
    public productGet(limit?: number, offset?: number, terms?: string, observe?: 'response', reportProgress?: boolean, criticalError?: boolean): Observable<HttpResponse<Array<Product>>>;
    public productGet(limit?: number, offset?: number, terms?: string, observe?: 'events', reportProgress?: boolean, criticalError?: boolean): Observable<HttpEvent<Array<Product>>>;
    public productGet(limit?: number, offset?: number, terms?: string, observe: any = 'body', reportProgress: boolean = false, criticalError: boolean = true ): Observable<any> {




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
        return this.httpClient.request<Array<Product>>('get',`${this.basePath}/product/`,
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
     * Retrieve a product
     * 
     * @param id The id of the account that needs to be fetched.
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     * @param criticalError flag to set whether an error on this request should me considered critical for the application flow
     */
    public productIdGet(id: number, observe?: 'body', reportProgress?: boolean, criticalError?: boolean): Observable<Product>;
    public productIdGet(id: number, observe?: 'response', reportProgress?: boolean, criticalError?: boolean): Observable<HttpResponse<Product>>;
    public productIdGet(id: number, observe?: 'events', reportProgress?: boolean, criticalError?: boolean): Observable<HttpEvent<Product>>;
    public productIdGet(id: number, observe: any = 'body', reportProgress: boolean = false, criticalError: boolean = true ): Observable<any> {

        if (id === null || id === undefined) {
            throw new Error('Required parameter id was null or undefined when calling productIdGet.');
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
        return this.httpClient.request<Product>('get',`${this.basePath}/product/${encodeURIComponent(String(id))}`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

}
