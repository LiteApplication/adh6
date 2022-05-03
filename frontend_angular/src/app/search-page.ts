import { BehaviorSubject, combineLatest, empty, merge, Observable, ReplaySubject } from 'rxjs';
import { debounceTime, distinctUntilChanged, map, shareReplay, switchMap } from 'rxjs/operators';
import { OnInit, Directive } from '@angular/core';
import { HttpResponse } from '@angular/common/http';
import { PagingConf } from './paging.config';

@Directive()
export class SearchPage<T> implements OnInit {
  private searchTerm$ = new BehaviorSubject<string>('');
  private pageNumber$ = new BehaviorSubject<number>(1);
  private httpGetter: (term: string, page: number) => Observable<HttpResponse<Array<T>>>;
  private shouldInitSearch: boolean;
  private cachedResult: Map<Number, Observable<Array<T>>> = new Map<Number, Observable<Array<T>>>();
  public maxItems: number;
  public itemsPerPage: number = +PagingConf.item_count;
  public result$: Observable<Array<T>>;

  constructor(f: (term: string, page: number) => Observable<HttpResponse<Array<T>>>, shouldInitSearch?: boolean) {
    this.httpGetter = f;
    this.shouldInitSearch = (shouldInitSearch != undefined) ? shouldInitSearch : true;
  }

  ngOnInit() {
    this.changePage(1);
    if (this.shouldInitSearch) {
      this.getSearchResult();
    }
  }

  protected getSearchResult(): void {
    // Stream of terms debounced
    const termsDebounced$ = this.searchTerm$
      .pipe(
        debounceTime(300),
        distinctUntilChanged(),
      );

    // Combine terms + page and fetch the result from backend
    const source$ = combineLatest([termsDebounced$, this.pageNumber$]);
    this.result$ = source$
      .pipe(
        switchMap(data => {
          if (!this.cachedResult.has(data[1])) {
            console.log("Begin caching data for page: " + data[1]);
            this.cachedResult.set(data[1], this.httpGetter(data[0], data[1])
              .pipe(
                shareReplay(1),
                map(response => {
                  const maxItems = +response.headers.get("x-total-count");
                  console.log("Data cached: " + response.body);
                  if (this.maxItems != maxItems) {
                    this.maxItems = maxItems;
                  }
                  return response.body;
                }),
              )
            )
            console.log("End caching data for page: " + data[1]);
          }
          return this.cachedResult.get(data[1]);
        }),
      );
  }

  private resetSearch() {
    this.cachedResult.clear();
  }

  public search(term: string): void {
    this.resetSearch();
    this.searchTerm$.next(term);
  }

  public changePage(page: number): void {
    this.pageNumber$.next(page);
  }
}
