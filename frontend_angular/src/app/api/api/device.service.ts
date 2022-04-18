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

import { AbstractDevice } from '../model/abstractDevice';
import { Device } from '../model/device';
import { Vendor } from '../model/vendor';

import { BASE_PATH, COLLECTION_FORMATS }                     from '../variables';
import { Configuration }                                     from '../configuration';


@Injectable()
export class DeviceService {

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
     * Filter devices
     * 
     * @param limit Limit the number of results returned
     * @param offset Skip the first n results
     * @param terms The generic search terms (will search in any field)
     * @param filter Filters by various properties
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     * @param criticalError flag to set whether an error on this request should me considered critical for the application flow
     */
    public deviceGet(limit?: number, offset?: number, terms?: string, filter?: any, observe?: 'body', reportProgress?: boolean, criticalError?: boolean): Observable<Array<Device>>;
    public deviceGet(limit?: number, offset?: number, terms?: string, filter?: any, observe?: 'response', reportProgress?: boolean, criticalError?: boolean): Observable<HttpResponse<Array<Device>>>;
    public deviceGet(limit?: number, offset?: number, terms?: string, filter?: any, observe?: 'events', reportProgress?: boolean, criticalError?: boolean): Observable<HttpEvent<Array<Device>>>;
    public deviceGet(limit?: number, offset?: number, terms?: string, filter?: any, observe: any = 'body', reportProgress: boolean = false, criticalError: boolean = true ): Observable<any> {





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
        return this.httpClient.request<Array<Device>>('get',`${this.basePath}/device/`,
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
     * Delete a device
     * 
     * @param id The id of the account that needs to be fetched.
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     * @param criticalError flag to set whether an error on this request should me considered critical for the application flow
     */
    public deviceIdDelete(id: number, observe?: 'body', reportProgress?: boolean, criticalError?: boolean): Observable<any>;
    public deviceIdDelete(id: number, observe?: 'response', reportProgress?: boolean, criticalError?: boolean): Observable<HttpResponse<any>>;
    public deviceIdDelete(id: number, observe?: 'events', reportProgress?: boolean, criticalError?: boolean): Observable<HttpEvent<any>>;
    public deviceIdDelete(id: number, observe: any = 'body', reportProgress: boolean = false, criticalError: boolean = true ): Observable<any> {

        if (id === null || id === undefined) {
            throw new Error('Required parameter id was null or undefined when calling deviceIdDelete.');
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
        return this.httpClient.request<any>('delete',`${this.basePath}/device/${encodeURIComponent(String(id))}`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Retrieve a device
     * 
     * @param id The id of the account that needs to be fetched.
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     * @param criticalError flag to set whether an error on this request should me considered critical for the application flow
     */
    public deviceIdGet(id: number, observe?: 'body', reportProgress?: boolean, criticalError?: boolean): Observable<Device>;
    public deviceIdGet(id: number, observe?: 'response', reportProgress?: boolean, criticalError?: boolean): Observable<HttpResponse<Device>>;
    public deviceIdGet(id: number, observe?: 'events', reportProgress?: boolean, criticalError?: boolean): Observable<HttpEvent<Device>>;
    public deviceIdGet(id: number, observe: any = 'body', reportProgress: boolean = false, criticalError: boolean = true ): Observable<any> {

        if (id === null || id === undefined) {
            throw new Error('Required parameter id was null or undefined when calling deviceIdGet.');
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
        return this.httpClient.request<Device>('get',`${this.basePath}/device/${encodeURIComponent(String(id))}`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Partially update a device
     * 
     * @param body The new values for this Device
     * @param id The id of the account that needs to be fetched.
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     * @param criticalError flag to set whether an error on this request should me considered critical for the application flow
     */
    public deviceIdPatch(body: AbstractDevice, id: number, observe?: 'body', reportProgress?: boolean, criticalError?: boolean): Observable<any>;
    public deviceIdPatch(body: AbstractDevice, id: number, observe?: 'response', reportProgress?: boolean, criticalError?: boolean): Observable<HttpResponse<any>>;
    public deviceIdPatch(body: AbstractDevice, id: number, observe?: 'events', reportProgress?: boolean, criticalError?: boolean): Observable<HttpEvent<any>>;
    public deviceIdPatch(body: AbstractDevice, id: number, observe: any = 'body', reportProgress: boolean = false, criticalError: boolean = true ): Observable<any> {

        if (body === null || body === undefined) {
            throw new Error('Required parameter body was null or undefined when calling deviceIdPatch.');
        }

        if (id === null || id === undefined) {
            throw new Error('Required parameter id was null or undefined when calling deviceIdPatch.');
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
        return this.httpClient.request<any>('patch',`${this.basePath}/device/${encodeURIComponent(String(id))}`,
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
     * Update a device
     * 
     * @param body The new values for this device
     * @param id The id of the account that needs to be fetched.
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     * @param criticalError flag to set whether an error on this request should me considered critical for the application flow
     */
    public deviceIdPut(body: AbstractDevice, id: number, observe?: 'body', reportProgress?: boolean, criticalError?: boolean): Observable<Device>;
    public deviceIdPut(body: AbstractDevice, id: number, observe?: 'response', reportProgress?: boolean, criticalError?: boolean): Observable<HttpResponse<Device>>;
    public deviceIdPut(body: AbstractDevice, id: number, observe?: 'events', reportProgress?: boolean, criticalError?: boolean): Observable<HttpEvent<Device>>;
    public deviceIdPut(body: AbstractDevice, id: number, observe: any = 'body', reportProgress: boolean = false, criticalError: boolean = true ): Observable<any> {

        if (body === null || body === undefined) {
            throw new Error('Required parameter body was null or undefined when calling deviceIdPut.');
        }

        if (id === null || id === undefined) {
            throw new Error('Required parameter id was null or undefined when calling deviceIdPut.');
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
        return this.httpClient.request<Device>('put',`${this.basePath}/device/${encodeURIComponent(String(id))}`,
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
     * Retrieve the vendor of a device based on its MAC
     * 
     * @param id The id of the account that needs to be fetched.
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     * @param criticalError flag to set whether an error on this request should me considered critical for the application flow
     */
    public deviceMabGet(id: number, observe?: 'body', reportProgress?: boolean, criticalError?: boolean): Observable<boolean>;
    public deviceMabGet(id: number, observe?: 'response', reportProgress?: boolean, criticalError?: boolean): Observable<HttpResponse<boolean>>;
    public deviceMabGet(id: number, observe?: 'events', reportProgress?: boolean, criticalError?: boolean): Observable<HttpEvent<boolean>>;
    public deviceMabGet(id: number, observe: any = 'body', reportProgress: boolean = false, criticalError: boolean = true ): Observable<any> {

        if (id === null || id === undefined) {
            throw new Error('Required parameter id was null or undefined when calling deviceMabGet.');
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
        return this.httpClient.request<boolean>('get',`${this.basePath}/device/${encodeURIComponent(String(id))}/mab/`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Retrieve the vendor of a device based on its MAC
     * 
     * @param id The id of the account that needs to be fetched.
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     * @param criticalError flag to set whether an error on this request should me considered critical for the application flow
     */
    public deviceMabPut(id: number, observe?: 'body', reportProgress?: boolean, criticalError?: boolean): Observable<boolean>;
    public deviceMabPut(id: number, observe?: 'response', reportProgress?: boolean, criticalError?: boolean): Observable<HttpResponse<boolean>>;
    public deviceMabPut(id: number, observe?: 'events', reportProgress?: boolean, criticalError?: boolean): Observable<HttpEvent<boolean>>;
    public deviceMabPut(id: number, observe: any = 'body', reportProgress: boolean = false, criticalError: boolean = true ): Observable<any> {

        if (id === null || id === undefined) {
            throw new Error('Required parameter id was null or undefined when calling deviceMabPut.');
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
        return this.httpClient.request<boolean>('put',`${this.basePath}/device/${encodeURIComponent(String(id))}/mab/`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Create device
     * 
     * @param body The device to create
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     * @param criticalError flag to set whether an error on this request should me considered critical for the application flow
     */
    public devicePost(body: Device, observe?: 'body', reportProgress?: boolean, criticalError?: boolean): Observable<Device>;
    public devicePost(body: Device, observe?: 'response', reportProgress?: boolean, criticalError?: boolean): Observable<HttpResponse<Device>>;
    public devicePost(body: Device, observe?: 'events', reportProgress?: boolean, criticalError?: boolean): Observable<HttpEvent<Device>>;
    public devicePost(body: Device, observe: any = 'body', reportProgress: boolean = false, criticalError: boolean = true ): Observable<any> {

        if (body === null || body === undefined) {
            throw new Error('Required parameter body was null or undefined when calling devicePost.');
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
        return this.httpClient.request<Device>('post',`${this.basePath}/device/`,
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
     * Retrieve the vendor of a device based on its MAC
     * 
     * @param id The id of the account that needs to be fetched.
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     * @param criticalError flag to set whether an error on this request should me considered critical for the application flow
     */
    public vendorGet(id: number, observe?: 'body', reportProgress?: boolean, criticalError?: boolean): Observable<Vendor>;
    public vendorGet(id: number, observe?: 'response', reportProgress?: boolean, criticalError?: boolean): Observable<HttpResponse<Vendor>>;
    public vendorGet(id: number, observe?: 'events', reportProgress?: boolean, criticalError?: boolean): Observable<HttpEvent<Vendor>>;
    public vendorGet(id: number, observe: any = 'body', reportProgress: boolean = false, criticalError: boolean = true ): Observable<any> {

        if (id === null || id === undefined) {
            throw new Error('Required parameter id was null or undefined when calling vendorGet.');
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
        return this.httpClient.request<Vendor>('get',`${this.basePath}/device/${encodeURIComponent(String(id))}/vendor`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

}
