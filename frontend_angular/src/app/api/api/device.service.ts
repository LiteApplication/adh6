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

import { Device } from '../model/device';
import { InlineResponse2001 } from '../model/inlineResponse2001';

import { BASE_PATH, COLLECTION_FORMATS }                     from '../variables';
import { Configuration }                                     from '../configuration';


@Injectable()
export class DeviceService {

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
     * Filter devices
     * 
     * @param limit Limit the number of devices returned in the result. Default is 100
     * @param offset Skip the first n results
     * @param username Filter by owner&#x27;s username
     * @param terms Search terms
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public deviceGet(limit?: number, offset?: number, username?: string, terms?: string, observe?: 'body', reportProgress?: boolean): Observable<Array<Device>>;
    public deviceGet(limit?: number, offset?: number, username?: string, terms?: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<Array<Device>>>;
    public deviceGet(limit?: number, offset?: number, username?: string, terms?: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<Array<Device>>>;
    public deviceGet(limit?: number, offset?: number, username?: string, terms?: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {





        let queryParameters = new HttpParams({encoder: new CustomHttpUrlEncodingCodec()});
        if (limit !== undefined && limit !== null) {
            queryParameters = queryParameters.set('limit', <any>limit);
        }
        if (offset !== undefined && offset !== null) {
            queryParameters = queryParameters.set('offset', <any>offset);
        }
        if (username !== undefined && username !== null) {
            queryParameters = queryParameters.set('username', <any>username);
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
     * @param macAddress The mac address of the device that will be deleted
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public deviceMacAddressDelete(macAddress: string, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public deviceMacAddressDelete(macAddress: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public deviceMacAddressDelete(macAddress: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public deviceMacAddressDelete(macAddress: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (macAddress === null || macAddress === undefined) {
            throw new Error('Required parameter macAddress was null or undefined when calling deviceMacAddressDelete.');
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
        ];

        return this.httpClient.request<any>('delete',`${this.basePath}/device/${encodeURIComponent(String(macAddress))}`,
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
     * @param macAddress The mac address of the device that will be fetched
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public deviceMacAddressGet(macAddress: string, observe?: 'body', reportProgress?: boolean): Observable<Device>;
    public deviceMacAddressGet(macAddress: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<Device>>;
    public deviceMacAddressGet(macAddress: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<Device>>;
    public deviceMacAddressGet(macAddress: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (macAddress === null || macAddress === undefined) {
            throw new Error('Required parameter macAddress was null or undefined when calling deviceMacAddressGet.');
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

        return this.httpClient.request<Device>('get',`${this.basePath}/device/${encodeURIComponent(String(macAddress))}`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Update/create a device
     * 
     * @param body Device to update
     * @param macAddress The mac address of the device that will be updated
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public deviceMacAddressPut(body: Device, macAddress: string, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public deviceMacAddressPut(body: Device, macAddress: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public deviceMacAddressPut(body: Device, macAddress: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public deviceMacAddressPut(body: Device, macAddress: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (body === null || body === undefined) {
            throw new Error('Required parameter body was null or undefined when calling deviceMacAddressPut.');
        }

        if (macAddress === null || macAddress === undefined) {
            throw new Error('Required parameter macAddress was null or undefined when calling deviceMacAddressPut.');
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

        return this.httpClient.request<any>('put',`${this.basePath}/device/${encodeURIComponent(String(macAddress))}`,
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
     * @param macAddress The mac address of the device that will be looked up
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public vendorGet(macAddress: string, observe?: 'body', reportProgress?: boolean): Observable<InlineResponse2001>;
    public vendorGet(macAddress: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<InlineResponse2001>>;
    public vendorGet(macAddress: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<InlineResponse2001>>;
    public vendorGet(macAddress: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (macAddress === null || macAddress === undefined) {
            throw new Error('Required parameter macAddress was null or undefined when calling vendorGet.');
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

        return this.httpClient.request<InlineResponse2001>('get',`${this.basePath}/device/${encodeURIComponent(String(macAddress))}/vendor`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

}
